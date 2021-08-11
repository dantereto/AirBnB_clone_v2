#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey, Table
from models.user import User
from models.city import City
from os import getenv

column_amenity = Column('amenity_id', String(60), ForeignKey('amenities.id'))
place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id')),
                      column_amenity)


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    if getenv("HBNB_TYPE_STORAGE") == "db":
        city_id = Column(String(60), ForeignKey(City.id), nullable=False)
        user_id = Column(String(60), ForeignKey(User.id), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=False)
        longitude = Column(Float, nullable=False)
        kwargs_reviews = {
            "secondary": place_amenity,
            "back_populates": "place_amenities",
            viewonly: False
        }
        amenities = relationship("Amenity", **kwargs_reviews)
        kwargs_reviews = {"cascade": "all, delete-orphan", "backref": "place"}
        reviews = relationship("Review", **kwargs_reviews)
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []
