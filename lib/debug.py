from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
import click
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref

engine = create_engine('sqlite:///todo_app.db')
Base = declarative_base()
session = sessionmaker(bind=engine)
session = session()




