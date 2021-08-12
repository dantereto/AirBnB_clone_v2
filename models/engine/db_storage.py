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
from os import getenv

class DBStorage():
    """ class to storage for database with MySQL """

    __engine = None
    __session = None

    def __init__(self):
        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        localhost = getenv('HBNB_MYSQL_HOST')
        database = getenv('HBNB_MYSQL_DB')
        DBStorage.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
            .format(user, password, localhost, database), pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        if cls is None:
            data = self.__session.query(City).all()
            data += self.__session.query(User).all()
            data += self.__session.query(State).all()
            data += self.__session.query(Place).all()
            data += self.__session.query(Amenity).all()
            data += self.__session.query(Review).all()
        else:
            data = self.__session.query(eval(cls)).all()
        result = {}
        for element in data:
            key = '{}.{}'.format(type(element).__name__, element.id)
            result[key] = element
        return (result)

    def new(self, obj):
        '''Add new element'''
        self.__session.add(obj)

    def save(self):
        '''Save transaction'''
        self.__session.commit()

    def delete(self, obj=None):
        '''Delete object '''
        if obj is not none:
            self.__session.delete(obj)

    def reload(self):
        '''Reload model'''
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        ScopSession = scoped_session(session)
        self.__session = ScopSession()
        
    def close(self):
        '''Delete object '''
        self.__session.remove()
