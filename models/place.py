#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Table, Column, Integer, Float, String, ForeignKey
from models.city import City
from models.user import User
from sqlalchemy.orm import relationship


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey(
                          'places.id'), primary_key=True, nullable=False),
                      Column('amenity_id', String(60), ForeignKey(
                          'amenities.id'), primary_key=True, nullable=False)
                      )


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    amenities = relationship(
        "Amenity", secondary=place_amenity, backref='amenities',
        viewonly=False)
    reviews = relationship("Review")

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        from models.review import Review
        from models.amenity import Amenity
        super().__init__(*args, **kwargs)

    @property
    def reviews(self):
        """Get reviews from FileStorage"""
        from models.review import Review
        from models import storage
        review_dict = storage.all(Review)
        review_list = list(review_dict.values())
        return [review for review in review_list
                if review.place_id == self.id]

    @property
    def amenities(self):
        """Get amenities from FileStorage"""
        from models.amenity import Amenity
        from models import storage
        amenity_dict = storage.all(Amenity)
        amenity_list = list(amenity_dict.values())
        return [amenity for amenity in amenity_list
                if amenity.id in self.amenity_ids]

    @amenities.setter
    def amenities(self, obj):
        """Set amenities to class attrib"""
        from models.amenity import Amenity
        if isinstance(obj, Amenity):
            self.amenities.append(obj.id)
