import click
import sqlite3
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship


engine = create_engine('sqlite:///todo_app.db')
Base = declarative_base()
session = sessionmaker(bind=engine)
session = session()


class Todo_list(Base):
    __tablename__ = 'tasks'
    id = Column("id", Integer, primary_key=True)
    name = Column("name", String)
    priority = Column("priority", String)
    tasks = relationship('Task', back_populates='todo_list')
    user = Column(Integer, ForeignKey('user'))
    
    def __init__(self, name, task, user):
        self.name = name
        self.task = task
        self.user = user

