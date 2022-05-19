from flask import Flask
from flask_bcrypt import Bcrypt

# Initializing application
app = Flask(__name__)
app.config['SECRET_KEY']='123'
bcrypt = Bcrypt(app)

from app import routes