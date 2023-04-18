# import click
# import sqlite3
# from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, CHAR
# from datetime import datetime
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker, relationship


# Base = declarative_base()


# class User(Base):
#     __tablename__ = 'User'
#     id = Column("id", Integer, primary_key=True)
#     name = Column("name", String)

#     def __init__(self, id, name):
#         self.id = id
#         self.name = name
        
#     def __repr__(self):
#         return f"({self.id}) {self.name}"



# engine = create_engine('sqlite:///todo_app.db')
# Base.metadata.create_all(bind=engine)

# session = sessionmaker(bind=engine)
# session = session()



# user1 = User(1,  "Nick")
# user2 = User(2, "Bob")
# user3 = User(3, "Jenna")
# user4 = User(44,  "Iggy")
# user5 = User(222, "Elif")
# user6 = User(89, "George")

# session.add_all([user1, user2, user3, user4, user5, user6])
# session.commit()
