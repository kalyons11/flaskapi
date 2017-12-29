from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy import ForeignKey, Column, Integer, String, Boolean
from sqlalchemy.orm import backref, relationship

from flaskapi import Base


class Author(Base):
    @declared_attr
    def __tablename__(cls):
        # API endpoint: /api/__tablename__
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)
    first_name = Column(String(64))
    last_name = Column(String(64))


class Book(Base):
    @declared_attr
    def __tablename__(cls):
        # API endpoint: /api/__tablename__
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)
    title = Column(String(64))
    author_id = Column(Integer, ForeignKey('author.id'), nullable=True)
    author = relationship(Author, backref=backref('books'))
    is_available = Column(Boolean)
