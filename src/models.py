import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)
class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    mail = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)

class Personajes(Base):
    __tablename__ = 'personajes'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    hair_color = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)

class Planetas(Base):
    __tablename__ = 'planetas'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    diameter = Column(Integer, nullable=False)
    population = Column(Integer, nullable=False)
    terrain = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)


class Favoritos(Base):
    __tablename__ = 'favoritos'

    id = Column(Integer, primary_key=True)

    User_id = Column(Integer, ForeignKey('user.id'))
    User = relationship(User)
    tipoFavorito = Column(String(250), nullable=False)
    favoritoId = Column(String(250), nullable=False)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')