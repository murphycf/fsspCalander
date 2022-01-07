from flask import Flask, render_template


fsspCalander = Flask(__name__)

@fsspCalander.route('/')
def calander():
    return render_template("index.html")