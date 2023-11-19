#!/usr/bin/python3
"""Definition of class City"""
from relationship_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    '''Class City'''
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement="auto", nullable= False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
