from flask import render_template, url_for
from app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin')
def admin_home():
    return render_template('admin_index.html')