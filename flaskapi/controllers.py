from flaskapi import manager
from flaskapi.models import Author, Book


METHODS = ['GET', 'PATCH', 'POST', 'DELETE']


author_blueprint = manager.create_api_blueprint(Author, methods=METHODS)
book_blueprint = manager.create_api_blueprint(Book, methods=METHODS)
