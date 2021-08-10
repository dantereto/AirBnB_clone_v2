#!/usr/bin/python3
""" City Module for HBNB project """

from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os

class DBStorage():

    __engine = None
    __session = None

    def __init__(self):
        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        localhost = os.getenv('HBNB_MYSQL_HOST', None)
        database = os.getenv('HBNB_MYSQL_DB', None)
        self.__engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                                      .format(user, password, database), pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        data = []
        if cls is None:
            entries = [City, User, Place, Amenity, Review]
            for entry in entries:
                data.append(self.__session.query(entry).all())
        else:
            data.append(self.__session.query(eval(cls)).all())
        result = {}
        for element in data:
            key = '{}.{}'.format(type(element).__name__, element.id)
            setattr(result, key, element)
        return (result)

    def new(self, obj):
        if obj:
            self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        ScopSession = scoped_session(session)
        self.__session = ScopSession()

    def close(self):
        self.__session.close()
