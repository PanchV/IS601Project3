"""A simple flask web app"""
import flask_login
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf.csrf import CSRFProtect

import os
from flask import Flask
from app.context_processors import utility_text_processors
from app.simple_pages import simple_pages
from app.auth import auth
from app.exceptions import http_exceptions
from app.db.models import User
from app.db import db
from app.auth import auth
from app.cli import create_database, create_log_folder

login_manager = flask_login.LoginManager()


def page_not_found(e):
    return render_template("404.html"), 404


def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    if app.config["ENV"] == "production":
        app.config.from_object("app.config.ProductionConfig")
    elif app.config["ENV"] == "development":
        app.config.from_object("app.config.DevelopmentConfig")
    elif app.config["ENV"] == "testing":
        app.config.from_object("app.config.TestingConfig")

    # https://flask-login.readthedocs.io/en/latest/  <-login manager
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"
    # Needed for CSRF protection of form submissions and WTF Forms
    # https://wtforms.readthedocs.io/en/3.0.x/
    csrf = CSRFProtect(app)
    # https://bootstrap-flask.readthedocs.io/en/stable/
    bootstrap = Bootstrap5(app)
    # these load functions with web interface
    app.register_blueprint(simple_pages)
    app.register_blueprint(auth)

    # these load functionality without a web interface
    app.register_blueprint(log_con)
    app.register_blueprint(error_handlers)
    app.context_processor(utility_text_processors)
    # add command function to cli commands
    app.cli.add_command(create_database)
    app.cli.add_command(create_log_folder)

    # Run once at startup:
    db.init_app(app)

    return app


@login_manager.user_loader
def user_loader(user_id):
    try:
        return User.query.get(int(user_id))
    except:
        return None
