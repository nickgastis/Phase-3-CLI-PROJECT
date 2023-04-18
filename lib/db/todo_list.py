import click
import sqlite3
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship



Base = declarative_base()


class Todo_list(Base):
    __tablename__ = 'tasks'
    id = Column("id", Integer, primary_key=True)
    name = Column("name", String)
    description = Column("description", String)
    priority = Column("priority", String)
    tasks = relationship('Task', back_populates='todo_list')
    user = Column(Integer, ForeignKey('user'))
    
    def __init__(self, id,  name, description, user):
        self.id = id
        self.name = name
        self.description = description
        self.user = user



engine = create_engine('sqlite:///todo_list.db')
Base.metadata.create_all(bind=engine)

session = sessionmaker(bind=engine)
session = session()

Trash = Todo_list(1, "Trash", "take out the trash", 44)


session.add_all([Trash])
session.commit()
