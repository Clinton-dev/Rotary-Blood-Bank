from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


# Initializing application
app = Flask(__name__)
app.config['SECRET_KEY'] = '123'
admin_user = 'prod'
if admin_user == 'hussein':
 app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:mwas6190@localhost/BRD_proto'
else:
 app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://tsqzjtlnbdbdwj:113d39149866c6cd7fab1d8eea04855b62469a982d875b1c257d55be4a2b3761@ec2-52-3-2-245.compute-1.amazonaws.com:5432/dcb7m5odvbp6e1'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'danger'
from app import routes

