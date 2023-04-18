from sqlalchemy import create_engine, Column, Interger, String, DateTime, ForeignKey
import click
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('sqlite:///todo_app.db')
Base = declarative_base()
session = sessionmaker(bind=engine)
session = session()



