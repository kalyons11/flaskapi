from flask import Flask
import flask_restless
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import *

# Create flask app
app = Flask(__name__)

# Create DB engine
engine = create_engine('sqlite:///foobar.db')
Session = sessionmaker(bind=engine, autocommit=False, autoflush=False)
s = scoped_session(Session)

Base = declarative_base()
Base.metadata.bind = engine

# Create all models
from flaskapi.models import Book, Author
Base.metadata.create_all()

# Set up restless
manager = flask_restless.APIManager(app, session=s)

# Register blueprints for CRUD endpoints
from flaskapi.controllers import author_blueprint, book_blueprint
app.register_blueprint(author_blueprint)
app.register_blueprint(book_blueprint)
