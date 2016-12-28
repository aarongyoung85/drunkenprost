from sqlalchemy import Column, Integer, String, DateTime, Text, Boolean, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKeyConstraint

Base = declarative_base()

class Topics(Base):
    __tablename__ = 'topics'

    id = Column(String, primary_key=True)
    topic = Column(String)

class Breweries(Base):
    __tablename__ = 'breweries'

    id = Column(String, primary_key=True)
    brewery = Column(String)

class BeerTypes(Base):
    __tablename__ = 'beer_types'

    id = Column(String, primary_key=True)
    beer_type = Column(String)

class Countries(Base):
    __tablename__ = 'countries'

    id = Column(String, primary_key=True)
    iso = Column(String)
    country = Column(String)

class Beers(Base):
    __tablename__ = 'beers'

    id = Column(String, primary_key=True)
    created = Column(DateTime)
    brewery = Column(String, ForeignKey('Breweries.id'))
    beer_type = Column(String, ForeignKey('BeerTypes.id'))
    country = Column(String, ForeignKey('Countries.id'))
    abv = Column(Float(precision=3, scale=1, asdecimal=True))
    link_name = Column(String, index=True)
    display_name = Column(String)

topics_map = {
    'beer': Beers
}
