from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
import click
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref

engine = create_engine('sqlite:///todo_app.db')
Base = declarative_base()
session = sessionmaker(bind=engine)
session = session()



#USERS
class User(Base):
    __tablename__ = 'users'
    id = Column("id", Integer, primary_key=True)
    name = Column("name", String)

    def __init__(self, id, name):
        self.id = id
        self.name = name
        
    def __repr__(self):
        return f"({self.id}) {self.name}"





#TOdo LISTS
class TodoList(Base):
    __tablename__ = 'todo_lists'
    id = Column("id", Integer, primary_key=True)
    name = Column("name", String)
    description = Column("description", String)
    priority = Column("priority", String)
    tasks = relationship('Task', backref='todo_list')
    user = Column(Integer, ForeignKey('users.id'))
    
    def __init__(self, id,  name, description, user):
        self.id = id
        self.name = name
        self.description = description
        self.user = user





#TASKS
class Task(Base):
    __tablename__ = 'tasks'
    id = Column("id", Integer, primary_key=True)
    name = Column("name", String)
    description = Column("description", String)
    due_date = Column("due_date", DateTime)
    completed_at = Column("completed_at", DateTime)
    todo_list_id = Column(Integer, ForeignKey('todo_lists.id'))
    # todo_list = relationship('TodoList', backref=backref('tasks'))
    
    def __init__(self, id,  name, description, due_date, completed_at):
        self.id = id
        self.name = name
        self.description = description
        self.due_date = due_date
        self.completed_at = completed_at





# user1 = User(1,  "Nick")
# user2 = User(2, "Bob")
# user3 = User(3, "Jenna")
# user4 = User(44,  "Iggy")
# user5 = User(222, "Elif")
# user6 = User(89, "George")


# session.add_all([user1, user2, user3, user4, user5, user6])
# session.commit()
