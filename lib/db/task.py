# import click
# import sqlite3
# from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
# from datetime import datetime
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker, relationship


# engine = create_engine('sqlite:///todo_app.db')
# Base = declarative_base()
# session = sessionmaker(bind=engine)
# session = session()

# class Task(Base):
#     __tablename__ = 'tasks'
#     id = Column("id", Integer, primary_key=True)
#     name = Column("name", String)
#     description = Column("description", String)
#     due_date = Column("due_date", DateTime)
#     completed_at = Column("completed_at", DateTime)
#     # todo_list = Column(Integer, ForeignKey('todo_list'))
#     todo_list = relationship('todo_list', back_populates='task')
    