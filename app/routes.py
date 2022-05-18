from flask import render_template, url_for
from app import app
from forms import LoginForm

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin')
def admin_home():
    return render_template('admin_index.html')


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)
@app.route('/donor')
def donor():
    return render_template('donors.html')

@app.route('/receiver')
def receiver():
    return render_template('receivers.html')

@app.route('/request')
def request():
    return render_template('request.html')
