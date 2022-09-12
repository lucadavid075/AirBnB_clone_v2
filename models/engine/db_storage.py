#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""


class DBStorage:
    """This class manages database storage of hbnb models"""
    __engine = None
    __session = None

    def __init__(self):
        import os
        from sqlalchemy import (create_engine)
        from models.base_model import Base, BaseModel
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            os.getenv('HBNB_MYSQL_USER'), os.getenv('HBNB_MYSQL_PWD'),
            os.getenv('HBNB_MYSQL_HOST'), os.getenv('HBNB_MYSQL_DB')),
            pool_pre_ping=True)
        Base.metadata.create_all(self.__engine)
