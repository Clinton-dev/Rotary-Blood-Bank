from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


# Initializing application
app = Flask(__name__)
app.config['SECRET_KEY'] = '123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:mwas6190@localhost/BRD_proto'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'danger'
from app import routes

