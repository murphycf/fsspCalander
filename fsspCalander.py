from flask import Flask, render_template


fsspCalender = Flask(__name__)

@app.route('/')
def calender():
    return render_template("index.html")