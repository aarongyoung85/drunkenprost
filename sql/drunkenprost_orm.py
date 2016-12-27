from sqlalchemy import Column, Integer, String, DateTime, Text, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKeyConstraint

Base = declarative_base()

class Topics(Base):
    __tablename__ = 'topics'

    id = Column(String, primary_key=True)
    topic = Column(String)
