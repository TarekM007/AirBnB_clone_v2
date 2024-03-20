#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import models
from models import storage


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    env_var = getenv('HBNB_TYPE_STORAGE')
    name = Column(String(128), nullable=False)
    cities = relationship("City",
                          backref="state", cascade="all, delete,delete-orphan")

    if env_var != "db":
        @property
        def cities(self):
            """ returns list of City instances related to state """
            list_of_cities = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    list_of_cities.append(city)
            return list_of_cities
