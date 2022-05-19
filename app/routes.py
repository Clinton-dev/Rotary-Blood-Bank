from flask import render_template, url_for,redirect,flash
from app import app, db
from app.forms import RegistrationForm, LoginForm
from app.models import Receiver, Donor, Waiting, User


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin_profile')
def admin_profile():
    return render_template('admin/admin_profile.html')

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
    if form.validate_on_submit():
        if form.email.data == 'user@gmail.com' and form.password.data == 'password':
            return redirect('index')
        

   
    return render_template ("user_register.html", title='Register', form=form)



@app.route('/donor')
def donor():
    donors = Donor.query.all()
    return render_template('admin/donors.html', donors= donors)

@app.route('/receiver')
def receiver():
    receivers = Receiver.query.all()
    return render_template('admin/receivers.html', receivers=receivers)

@app.route('/request')
def request():
    donors = Donor.query.all()
    receivers = Receiver.query.all()
 
    found = []

    for r in receivers:
        f = True
        if f :
            for d in donors:
                if r.blood_type == d.blood_type:
                    found.append([r, d])
                    f = False
                    break
        if f :
            for o in range(0, len(donors)):
                if donors[o].blood_type == 'O-':
                    found.append([r, donors[o]])
                    break
    return render_template('admin/request.html', found=found)


@app.route("/connect/<rec_id>/<don_id>", methods=['POST'])
def connect(rec_id, don_id):
    receiver = Receiver.query.get_or_404(rec_id)
    donor = Donor.query.get_or_404(don_id)
    waiting = Waiting(username=receiver.username, age=receiver.age, conditions=receiver.conditions, 
                      blood_type=receiver.blood_type, matched_blood=donor.blood_type, 
                      matched_username=donor.username, email=receiver.email)
    db.session.add(waiting)
    db.session.commit()
    
    db.session.delete(receiver)
    db.session.delete(donor)
    db.session.commit()
    return redirect(url_for('request'))

@app.route('/waiting_list')
def waiting_list():
    waitings = Waiting.query.all()
    return render_template('admin/wait.html', waitings=waitings)

@app.route("/done/<done_id>/", methods=['POST'])
def done(done_id):
    waiting = Waiting.query.get_or_404(done_id)
    db.session.delete(waiting)
    db.session.commit()
    return redirect(url_for('waiting_list'))
