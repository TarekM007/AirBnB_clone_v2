#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
import models
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable = False)
        cities = relationship("City",
                          backref="state", cascade="all, delete,delete-orphan")

        @property
        def cities(self):
            """ returns list of City instances related to state """
            from models import storage
            list_of_cities = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    list_of_cities.append(city)
            return list_of_cities
