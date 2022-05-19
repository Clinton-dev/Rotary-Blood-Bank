from flask import render_template, url_for, flash, redirect
from app import app
from app.forms import LoginForm


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin')
def admin_home():
    return render_template('admin_index.html')


@app.route('/adminlogin', methods=['GET','POST'])
def adminlogin():
    form = LoginForm()
    
    if form.validate_on_submit():
        print(form.email.data)
        print(form.password.data)
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('admin_home'))
        else:
            flash('Login Unsuccesfull. Please check username and password', 'danger')
        
    return render_template('adminlogin.html', title='admin Login', form=form)


@app.route('/donor')
def donor():
    return render_template('donors.html')

@app.route('/receiver')
def receiver():
    return render_template('receivers.html')

@app.route('/request')
def request():
    return render_template('request.html')
