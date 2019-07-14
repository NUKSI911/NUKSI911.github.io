import os
from flask import Flask,Blueprint
from flask_sqlalchemy import SQLAlchemy
from   flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from first_tutorial.config import Config


db= SQLAlchemy()
bcrypt=Bcrypt()
login_manager= LoginManager()
login_manager.login_view='users.login'
login_manager.login_message_category='info'

mail=Mail()




def create_app(config_class=Config):	
	app= Flask(__name__)
	app.config.from_object(Config)
	db.init_app(app)
	bcrypt.init_app(app)
	login_manager.init_app(app)
	mail.init_app(app)
	app.register_blueprint(users)
	app.register_blueprint(main)
	app.register_blueprint(posts)
	app.register_blueprint(errors)
	return app

from first_tutorial.users.routes import users
from first_tutorial.main.routes import main
from first_tutorial.posts.routes import posts
from first_tutorial.errors.handler import errors



	