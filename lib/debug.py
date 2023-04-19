from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
import click
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref
from db.models import (Base, User, TodoList, Task)

if __name__ == '__main__':
    engine = create_engine('sqlite:///todo_app.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()


# click.echo("Welcome to your ToDo-List! Please log in by running python debug.py log-in")

@click.group()
def mycommands():
    pass


# LOG-IN
@click.command()
@click.option("--name", prompt="Enter your name: ", help="The name of the user")
def log_in(name):
    user = User(name=name)
    session.add(user)
    session.commit()  # add commit method here
    click.clear()
    click.echo(f"Hello {name}!")
    click.echo(f"Please enter your next command. (Run python debug.py --help to view comands)")

    #add get or create
    
    # def get_or_create(session, model, **kwargs):
    # instance = session.query(model).filter_by(**kwargs).first()
    # if instance:
    #     return instance
    # else:
    #     instance = model(**kwargs)
    #     session.add(instance)
    #     session.commit()
    #     return instance


PRIORITIES = {
    "o": "Optional",
    "l": "Low",
    "m": "Medium",
    "h": "High",
    "c": "Crucial"
}

#ADD-ToDo-LIST
@click.command()
@click.argument("priority", type=click.Choice(PRIORITIES.keys()), default="m")
@click.option("-n", "--name", prompt="Enter the todo-list name: ", help="The name of the todo-list")
@click.option("-d", "--description", prompt="Describe the task: ", help="the description of the todo-list")
@click.option("-p", "--priority", prompt="Set priority: ", help="The priority of the todo-list", default="m")
def add_todo_list(name, description, priority):
    task = TodoList(name=name, description=description, priority=PRIORITIES[priority])
    session.add(task)
    session.commit()  # add commit method here
    click.clear()
    click.echo(f"ToDo-List created successfully!")
    click.echo(f"Please enter your next command. (Run python debug.py --help to view comands)")




#ADD-TASK
@click.command()
@click.argument("priority", type=click.Choice(PRIORITIES.keys()), default="m")
@click.option("-n", "--name", prompt="Enter the task name: ", help="The name of the task item")
@click.option("-d", "--description", prompt="Describe the task: ", help="the description of the task item")
@click.option("-p", "--priority", prompt="Set priority: ", help="The priority of the task item", default="m")
def add_task(name, description, priority):
    task = Task(name=name, description=description, priority=PRIORITIES[priority])
    session.add(task)
    session.commit()  # add commit method here
    click.clear()
    click.echo(f"Task added successfully!")
    click.echo(f"Please enter your next command. (Run python debug.py --help to view comands)")

    

# DELETE-TASK
@click.command()
# @click.argument("priority", type=click.Choice(PRIORITIES.keys()), default="m")
@click.argument("idx", type=int, required=False)
def delete_task(idx):
    tasks = session.query(Task).all()
    if not tasks:
        click.clear()
        click.echo("No tasks found.")
    else:
        for task in tasks:
            
            click.echo(f"ID: {task.id} | Description: {task.description} | Priority: {task.priority}")
        if not idx:
            
            idx = click.prompt("Enter the ID of the Task to delete", type=int)
        task = session.query(Task).filter_by(id=idx).first()
        if task:
            
            session.delete(task)
            session.commit()
            click.echo(f"Task with ID {idx} deleted successfully!")
            click.echo(f"Please enter your next command. (Run python debug.py --help to view comands)")


        else:
            click.echo(f"No Task found with ID {idx}.")


# DELETE-TDDO-List
@click.command()
# @click.argument("priority", type=click.Choice(PRIORITIES.keys()), default="m")
@click.argument("idx", type=int, required=False)
def delete_todo_list(idx):
    todo_lists = session.query(TodoList).all()
    if not todo_lists:
        click.clear()
        click.echo("No Todo-Lists found.")
    else:
        for todo_list in todo_lists:
            click.echo(f"ID: {todo_list.id} | Name: {todo_list.name}")
        if not idx:
            idx = click.prompt("Enter the ID of the Todo-List to delete", type=int)
        task = session.query(TodoList).filter_by(id=idx).first()
        if task:
            click.clear()
            session.delete(task)
            session.commit()
            click.echo(f"Todo-List with ID {idx} deleted successfully!")
            click.echo(f"Please enter your next command. (Run python debug.py --help to view comands)")
        else:
            click.echo(f"No Todo-List found with ID {idx}.")



mycommands.add_command(log_in)
mycommands.add_command(add_task)
mycommands.add_command(add_todo_list)
mycommands.add_command(delete_task)
mycommands.add_command(delete_todo_list)




if __name__ == "__main__":
    mycommands()




















# user1 = User(name = "Nick")
# user2 = User(name = "Bob")
# user3 = User(name = "Jenna")
# user4 = User(name = "Iggy")
# user5 = User(name = "Elif")
# user6 = User(name = "George")

# session.add(user1)
# session.add(user2)
# session.add(user3)
# session.add(user4)
# session.add(user5)
# session.add(user6)

# session.commit()