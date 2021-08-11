#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from os import getenv
from models.engine.db_storage import DBStorage

import os

if os.getenv('HBNB_TYPE_STORAGE') == 'db':
if getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage = DBStorage()
    storage.reload()
else:
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage = FileStorage()
    storage.reload()
storage.reload()
