import email
from email import message
from fileinput import filename
from urllib import request
from flask import Flask, render_template, send_from_directory, url_for, request, redirect
import csv
import os
app = Flask(__name__)

@app.route("/")
def my_home():
    return render_template('index.html')

@app.route("/<string:routelink>")
def my_works(routelink):
    return render_template(routelink)

@app.route("/<username>/<int:post_id>")
def hello_user(username=None, post_id=None):
    return render_template('index.html', name=username, post_id=post_id)

@app.route("/<username>")
def hello_use(username=None):
    return render_template('index.html', name=username)


def write_to_file(data):
    with open('database.txt', mode = 'a') as database:
        email = data["email"]
        message = data["message"]
        subject = data["subject"]
        file = database.write(f'\n{email},{subject}, {message}')

def write_to_csv(data):
    with open('database.csv', mode = 'a', newline ='') as database2:
        email = data["email"]
        message = data["message"]
        subject = data["subject"]
        csvwriter= csv.writer(database2, delimiter = ",", quotechar = '"', quoting = csv.QUOTE_MINIMAL)
        csvwriter.writerow([email, subject,message])

@app.route("/submit_form", methods = ['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data=request.form.to_dict()
        write_to_csv(data)
        return redirect("/thanks.html")
    else:
        return "something went wrong, try again" 