from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref

engine = create_engine('mysql://clive:password@localhost:3306/clio', echo=True)

Base = declarative_base()

class Country(Base):
 __tablename__ = 'country'

 id = Column(Integer, primary_key=True)
 name = Column(String)
 
 market = relationship("Market")
 
 def __repr__(self):
  return "<Country(name='%s')>" % (self.name)

class Market(Base):
 __tablename__ = 'market'

 id = Column(Integer, primary_key=True)
 name = Column(String)
 symbol = Column(String)
 is_survivor = Column(Boolean)
 country_id = Column(Integer, ForeignKey('country.id'))
 
 def __repr__(self):
  return "<Market(name='%s')>" % (self.name)


