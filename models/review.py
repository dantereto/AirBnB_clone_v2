#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from models.base_model import Base, BaseModel
from os import getenv


class Review(BaseModel, Base):
    """ Review classto store review information """
    __tablename__ = 'reviews'

    if getenv("HBNB_TYPE_STORAGE") == "db":
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('user.id'), nullable=False)
        text = Column(String(1024), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""
