from flask import Flask, request, jsonify, Response, render_template, redirect, url_for
app = Flask(__name__)
@app.route("/")
def show():
    return render_template("EcoPulse.html")