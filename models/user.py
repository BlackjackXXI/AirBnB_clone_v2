#!/usr/bin/python3
"""user update"""
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
 
class User(BaseModel, Base):
    """ This class represents a user with the following attributes:
    email, password, name and last name
    """

    __tablename__ = "users"
    
    if getenv("HBNB_TYPE_STORAGE", "fs") == "db":
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", backref="user", cascade="all, delete, delete-orphan")
        reviews = relationship("Review", backref="user", cascade="all, delete, delete-orphan")
    
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""