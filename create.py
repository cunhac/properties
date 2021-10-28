from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///lofts_register.db", echo=False)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class Lofts(Base):
    __tablename__ = 'lofts'

    id = Column(Integer, primary_key=True)
    state = Column(String(50))
    city = Column(String(50))
    district = Column(String(50))
    address = Column(String(70))
    number = Column(Integer)
    floor = Column(Integer)
    size_m2 = Column(Float)
    garage = Column(Integer)
    value = Column(Float)
    condominium = Column(Float)
    iptu = Column(Float)
    total_value = Column(Float)
    status = Column(String(50))


Base.metadata.create_all(engine)
