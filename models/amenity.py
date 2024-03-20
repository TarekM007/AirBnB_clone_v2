#!/usr/bin/python3
""" State Module for the HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """class for amenities"""
    __tablename__ = 'amenities'
    env_var = getenv("HBNB_TYPE_STORAGE")
    if env_var == "db":
        name = Column(String(128), nullable=False)
        place_amenity = relationship("Place", secondary="place_amenity",
                                       back_populates="amenities")
    else:
        name = ""
