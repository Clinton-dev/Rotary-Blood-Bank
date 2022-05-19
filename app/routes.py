from flask import render_template, url_for,redirect,flash
from app import app
from app.forms import RegistrationForm, LoginForm

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

@app.route('/admin_profile')
def admin_profile():
    return render_template('admin/admin_profile.html')

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

    

@app.route('/user_register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    return render_template ("user_register.html", title='Register', form=form)
@app.route('/donor')
def donor():
    return render_template('admin/donors.html')

@app.route('/receiver')
def receiver():
    return render_template('admin/receivers.html')

@app.route('/request')
def request():
    return render_template('admin/request.html',requests=patient_request)
