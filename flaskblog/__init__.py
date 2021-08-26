from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '87fa3bace7d1f472fba62cd58352f30f'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///site.db"
db = SQLAlchemy(app) # sql
bcrypt = Bcrypt(app) # encrypt password
login_manager = LoginManager(app)
login_manager.login_view = 'login' # redirect to login if not logged in
login_manager.login_message_category = 'info'

from flaskblog import routes