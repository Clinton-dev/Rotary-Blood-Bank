from flask import render_template, url_for,redirect,flash, request
from app import app, db
from app.forms import RegistrationForm, LoginForm, ReDO
from app.models import Receiver, Donor, Waiting, User
from flask_login import login_user, current_user, logout_user, login_required
from datetime import datetime

@app.route('/')
def landing_page():
    form = ReDO()
    return render_template('landingpage.html', form=form)

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
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            flash(f'{user.username}, You have been logged in!', 'secondary')
            if user.admin == 'no':
                return redirect(url_for('landing_page'))
            else:
                return redirect(url_for('admin_profile'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title = 'Login', form = form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('landing_page'))

    

@app.route('/user_register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        print('valid')
        print(form.username.data)
        blood_type = form.bloodgroup.data.upper()
        user = User(username=form.username.data, blood_type=blood_type, age=form.age.data,
                    email=form.email.data, conditions=form.conditions.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('created account', 'primary')
        return redirect(url_for('landing_page'))
        

   
    return render_template ("user_register.html", title='Register', form=form)

@app.route("/receive_data/<id>", methods=['POST'])
def receive_data(id):
    user = User.query.get(id)
    form = ReDO()
    choice = form.choice.data
    print(choice)
    print(id)
    if choice == 'Receive':
        rec = Receiver(username=user.username, conditions=user.conditions, blood_type=user.blood_type, email=user.email, age=user.age, date_requested=datetime.now())
        db.session.add(rec)
        db.session.commit()
        
    elif choice == 'Donate':
        don = Donor(username=user.username, conditions=user.conditions, blood_type=user.blood_type, email=user.email, age=user.age, date_requested=datetime.now())
        db.session.add(don)
        db.session.commit()
        
    
    return redirect(url_for('landing_page'))



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
