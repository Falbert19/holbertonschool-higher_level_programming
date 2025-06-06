#!/usr/bin/python3
"""Defines the State class mapped to
the states table using SQLAlchemy ORM."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create the declarative base
Base = declarative_base()

class State(Base):
    """State class that represents the `states` table in MySQL."""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
