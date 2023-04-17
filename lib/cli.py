import click

@click.group()
def mycommands():
    pass



#HELLO
@click.command()
@click.option("--name", prompt="Enter you name: ", help="The name of the user")
def hello(name):
    click.echo(f"Hello {name}!")


PRIORITIES = {
    "o": "Optional",
    "l": "Low",
    "m": "Medium",
    "h": "High",
    "c": "Crucial"
}

#ADD
@click.command()
@click.argument("priority", type=click.Choice(PRIORITIES.keys()), default="m")
@click.argument("todofile", type=click.Path(exists=False), required=False)
@click.option("-n", "--name", prompt="Enter the todo name: ", help="The name of the todo item")
@click.option("-d", "--description", prompt="Describe the todo: ", help="the dercription of the todo item")
@click.option("-p", "--priority", prompt="set priority: ", help="the priority of the todo item", default="m")


def add_todo(name, description, priority, todofile):
    filename = todofile if todofile is not None else "mytodos.txt"
    with open(filename, "a+") as f:
        f.write(f"{name}: {description} [Priority: {PRIORITIES[priority]}]\n")


#DELETE
@click.command()
@click.argument("idx", type=int, required=True)
# @click.option("-i", "--index", prompt="ToDo id: ", help="Provide Todo Id")
def delete_todo(idx):
    with open("mytodos.txt", "r") as f:
        todo_list = f.read().splitlines()
        todo_list.pop(idx)
    with open("mytodos.txt", "w") as f:
        f.write("\n".join(todo_list))
        f.write("\n")


#LIST
@click.command()
@click.option("-p", "--priority", type=click.Choice(PRIORITIES.keys()))
@click.argument("todofile", type=click.Path(exists=True), required=False)
def list_todos(priority, todofile):
    filename = todofile if todofile is not None else "mytodos.txt"
    with open(filename, "r") as f:
        todo_list = f.read().splitlines()
    if priority is None:
        for idx, todo in enumerate(todo_list):
            click.echo(f"({idx}) - {todo}")
    else:
        for idx, todo in enumerate(todo_list):
            if f"[Priority: {PRIORITIES[priority]}]" in todo:
                click.echo(f"({idx}) - {todo}")


mycommands.add_command(hello)
mycommands.add_command(add_todo)
mycommands.add_command(delete_todo)
mycommands.add_command(list_todos)


if __name__ == "__main__":
    mycommands()