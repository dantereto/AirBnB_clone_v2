#!/usr/bin/python3
""" City Module for HBNB project """
from models.state import State
from models.base_model import BaseModel
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import Base, BaseModel
from os import getenv
class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'

    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey(State.id), nullable=False)
        places = relationship(
            "Place", cascade="all, delete-orphan", backref='city')
    else:
        place_id = ""
        user_id = ""
        text = ""
