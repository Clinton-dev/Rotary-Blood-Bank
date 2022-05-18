from flask import render_template, url_for
from app import app

patient_request = [
    {"username":"john waweru","blood":"A"},
    {"username":"john waweru","blood":"A"},
    {"username":"james andwer","blood":"B"},
    {"username":"Peter waweru","blood":"A"},
    {"username":"john waweru","blood":"B"},
    {"username":"john waweru","blood":"AB"},
    {"username":"john waweru","blood":"O"}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin')
def admin_home():
    return render_template('admin_index.html')

@app.route('/donor')
def donor():
    return render_template('donors.html')

@app.route('/receiver')
def receiver():
    return render_template('receivers.html')

@app.route('/request')
def request():
    return render_template('request.html',requests=patient_request)