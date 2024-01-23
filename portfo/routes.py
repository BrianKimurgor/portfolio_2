from flask import Flask, url_for, render_template
from portfo import app



@app.route('/')
def home():
    return render_template('index.html')
