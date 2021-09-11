#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import Base, BaseModel
from sqlalchemy.orm import relationship
from models.base_model import BaseModel
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        cities = relationship(
            "City", cascade="all, delete-orphan", backref='state')
    else:
        name = ""
    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """Get a list of all related City objects."""
            city_list = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
