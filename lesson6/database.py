from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

url = 'postgresql://postgres:postgres@localhost:5433/postgres'

engine = create_engine(url)
session = Session(engine)