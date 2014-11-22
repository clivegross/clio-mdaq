from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Boolean, Decimal, TimeStamp
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref

conn_string = 'mysql://clio:clio@localhost:3306/clio'

engine = create_engine(conn_string, echo=True)

Base = declarative_base()

class Country(Base):
 __tablename__ = 'country'

 id = Column(Integer, primary_key=True)
 name = Column(String)
 
 market = relationship("Market", backref='country')
 
 def __repr__(self):
  return "<Country(name='%s')>" % (self.name)

class Market(Base):
 __tablename__ = 'market'

 id = Column(Integer, primary_key=True)
 name = Column(String)
 symbol = Column(String)
 is_survivor = Column(Boolean)
 country_id = Column(Integer, ForeignKey('country.id'))
 
 companies = relationship("Company", secondary="market_company_maps", backref="markets")
 
 def __repr__(self):
  return "<Market(name='%s', symbol='%s', is_survivor='%s', country_id='%s')>" % (self.name, self.symbol, self.is_survivor)
  
class Company(Base):
 __tablename__ = 'company'

 id = Column(Integer, primary_key=True)
 name = Column(String)
 symbol = Column(String)
 is_survivor = Column(Boolean)
 industry_id = Column(Integer, ForeignKey('industry.id'))
 
 prices = relationship("Price", backref="companies")
 announcements = relationship("Announcement", backref="companies")
 casualties = relationship("Casualty", uselist=False, backref="companies")
 
 def __repr__(self):
  return "<Company(name='%s', symbol='%s', is_survivor='%s', industry_id='%s')>" % (self.name, self.symbol, self.is_survivor, self.industry_id)
  
class MarketCompanyMaps(Base):
    __tablename__ = 'market_company_maps'

    market_id = Column(Integer, ForeignKey('market.id'), primary_key=True)
    company_id = Column(Integer, ForeignKey('company.id'), primary_key=True)


class Industry(Base):
 __tablename__ = 'industry'

 id = Column(Integer, primary_key=True)
 name = Column(String)
 
 companies = relationship("Company", secondary="industry_company_maps", backref="industries")
 
 def __repr__(self):
  return "<Industry(name='%s')>" % (self.name)
  
class IndustryCompanyMaps(Base):
    __tablename__ = 'industry_company_maps'

    industry_id = Column(Integer, ForeignKey('industry.id'), primary_key=True)
    company_id = Column(Integer, ForeignKey('company.id'), primary_key=True)

class Price(Base):
 __tablename__ = 'price'

 id = Column(Integer, primary_key=True)
 company_id = Column(Integer, ForeignKey('company.id'))
 timestamp_utc = Column(Timestamp)
 high = Column(Decimal)
 low = Column(Decimal)
 open = Column(Decimal)
 close = Column(Decimal)
 volume = Column(Integer)
 
 def __repr__(self):
  return "<Industry(name='%s')>" % (self.name)





