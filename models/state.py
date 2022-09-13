#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City")

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        from models.city import City
        super().__init__(*args, **kwargs)

    @property
    def cities(self):
        """Get cities for FileStorage"""
        from models.city import City
        from models import storage
        city_dict = storage.all(City)
        city_list = list(city_dict.values())
        return [city for city in city_list if city.state_id == self.id]
