from app import db, login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    blood_type = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    conditions = db.Column(db.Text, nullable=False, default='Thank God am healthy')
    admin = db.Column(db.String(20), nullable=False, default='no')
    date_joined = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
class Receiver(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    blood_type = db.Column(db.String(20), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    conditions = db.Column(db.Text, nullable=False, default='Thank God am healthy')
    email = db.Column(db.String(120), unique=True, nullable=False)
    date_requested = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"
    
class Donor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    conditions = db.Column(db.Text, nullable=False, default='Thank God am healthy')
    blood_type = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    date_requested = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    
class Waiting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    conditions = db.Column(db.Text, nullable=False, default='Thank God am healthy')
    blood_type = db.Column(db.String(20), nullable=False)
    matched_blood = db.Column(db.String(20), nullable=False)
    matched_username = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    date_requested = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)