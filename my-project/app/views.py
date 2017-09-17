from flask import render_template, request

from app import app

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/seqlength', methods=['GET', 'POST'])
def seqlength():
    return render_template("seqlength.html")


@app.route('/output')
def output():
    return render_template("output.html")
