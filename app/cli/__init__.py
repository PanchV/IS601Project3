import click
from flask.cli import with_appcontext
from app.db import db
import os

@click.command(name='create-log-folder')
@with_appcontext
def create_log_folder():
    """ create log directory """
    root = os.path.dirname(os.path.abspath(__file__))
    logdir = os.path.join(root, '../logs')
    if not os.path.exists(logdir):
        os.mkdir(logdir)


@click.command(name='create-db')
@with_appcontext
def create_database():
    """ create database directory """
    root = os.path.dirname(os.path.abspath(__file__))
    dbdir = os.path.join(root, '../../database')
    if not os.path.exists(dbdir):
        os.mkdir(dbdir)
    #db.create_all()