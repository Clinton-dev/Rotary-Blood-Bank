from flask import render_template, url_for,redirect
from app import app
from forms import RegistrationForm

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin')
def admin_home():
    return render_template('admin_index.html')



@app.route('/user_register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    return render_template ("user_register.html", title='Register', form=form)