from flask import render_template, url_for,flash,redirect,request
from app import app
from app.forms import LoginForm

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin')
def admin_home():
    return render_template('admin_index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "user@gmail.com" and form.password.data == "password":
            flash('login unsuccessful', 'danger')
            return redirect(url_for('index'))
    return render_template('login.html', title = 'Login', form = form)

@app.route("/logout")
def logout():
    return redirect(url_for('home'))

    