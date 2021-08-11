#!/usr/bin/python3
""" State Module for HBNB project """

from models.base_model import Base, BaseModel
from sqlalchemy.orm import relationship
from models.base_model import BaseModel
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from os import getenv
import models

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                          cascade="all, delete-orphan")
    else:
        name = ""

    @property
    def cities(self):
        list_cities = []
        for city in models.storage.all(City):
            if city.state_id == self.id:
                list_cities.append(city)
        return (list_cities)
