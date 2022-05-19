from flask import Flask

# Initializing application
app = Flask(__name__)
app.config['SECRET_KEY'] = '123'

from app import routes

