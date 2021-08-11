#!/usr/bin/python3
""" State Module for HBNB project """

from models.base_model import Base, BaseModel
from sqlalchemy.orm import relationship
from models.base_model import BaseModel
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from os import getenv

class State(BaseModel):
    """ State class """
    __tablename__ = 'states'
    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        kwargs = {"cascade": "all, delete-orphan", "backref": "state"}
        cities = relationship("City", **kwargs)
    else:
        name = ""

    @property
    def cities(self):
        """returns the list of City instances with state_id"""
        from models import storage
        from models.city import City
        # refactor to for list return ([for])
        list_cities = []
        for city in storage.all(City):
            if city.state_id == self.id:
                list_cities.append(city)
        return (list_cities)
