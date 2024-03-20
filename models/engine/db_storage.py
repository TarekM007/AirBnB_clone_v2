#!/usr/bin/python3
""" file storage class for AirBnB """
import models
from models.base_model import Base
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import getenv
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """SQL database storage"""
    __engine = None
    __session = None

    def __init__(self):
        """Creates engine"""
        SQL_user = getenv("HBNB_MYSQL_USER")
        SQL_pwd = getenv("HBNB_MYSQL_PWD")
        SQL_host = getenv("HBNB_MYSQL_HOST")
        SQL_db = getenv("HBNB_MYSQL_DB")
        SQL_envv = getenv("HBNB_ENV", "none")

        self.__engine = create_engine(f"mysql+mysqldb://{SQL_user}:{SQL_pwd}@{SQL_host}/{SQL_db}"
            , pool_pre_ping = True)

        if SQL_envv == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current database session (self.__session)"""

        dic = {}
        if not cls:
            class_table = [User, State, City, Amenity, Place, Review]

        else:
            if type(cls) == str:
                cls = eval(csl)

            class_table = [cls]

        for item in class_table:
            query = self.__session.query(item).all()

            for elem in query:
                key = "{}.{}".format(type(elem).__name__, elem.id)
                dic[key] = elem

        return dic

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database (feature of SQLAlchemy)"""
        self.__session = Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
