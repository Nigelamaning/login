from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__, template_folder="templates")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success")
def index():
    return render_template("success.html")
