import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    user_id = Column(String(250), nullable=False, primary_key=True)
    name = Column(String(250), nullable=False)


class Favorite(Base):
    __tablename__ = 'favorite'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    name = Column(String(250), nullable=False, primary_key=True)
    user_id= Column(String(250), ForeignKey('User'))
    people_id = Column(Integer, ForeignKey('people.people_id'))
    vehicle_id = Column(Integer, ForeignKey('vehicles.vehicle_id'))
    planet_id = Column(Integer, ForeignKey('planets.planet_id'))
    user = relationship(User)


class People(Base):
    __tablename__ = 'people'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    people_id = Column(Integer, primary_key=True)
    people_name = Column(String(250), nullable=False)
    heigh = Column(Integer)
    mass = Column(Integer)
    hair_color = Column(String(80))
    skin_color = Column(String(80))
    eye_color = Column(String(80))
    birth_year = Column(String(80))
    gender = Column(String(80))
    favorite = relationship(Favorite)


class Vehicles(Base):
    __tablename__ = 'vehicles'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    vehicle_id = Column(Integer, primary_key=True)
    vehicle_name = Column(String(250), nullable=False)
    model = Column(String(80))
    manufacturer = Column(String(80))
    cost_in_credits = Column(Integer)
    length = Column(Integer)
    max_atmosphering_speed = Column(Integer)
    crew = Column(String(80))
    passengers = Column(Integer)
    cargo_capacity = Column(Integer)
    consumables = Column(String)
    favorite = relationship(Favorite)

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    planet_id = Column(Integer, primary_key=True)
    planet_name = Column(String(250), nullable=False)
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    diameter = Column(Integer)
    climate = Column(String)
    gravity = Column(String)
    terrain = Column(String(80))
    surface_water = Column(String)
    population = Column(Integer)
    favorite = relationship(Favorite)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
