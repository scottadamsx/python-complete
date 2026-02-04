#! usr/bin/env python3
from guizero import App, ButtonGroup, CheckBox, Box 
"task: create a simple to do list"

FILENAME = "todo_list.txt"

def read_todo(FILENAME):
    todo = []
    try:
        with open(FILENAME, "r") as file:
            for row in file:
                todo.append(row)

        return todo
    except FileNotFoundError:
        with open(FILENAME, "w") as file:
            file.write()
        print("file didnt exist, created one for ya")

def add_todo(todo):
    newTodo = input("Choose something to add to the list: ")
    todo.append(newTodo)


def write_todo(FILENAME,todo):
    with open(FILENAME, "w") as file:
        for i in todo:
            file.write(f"{i}\n")
    print("File has been updated")


todo = read_todo(FILENAME)
add_todo(todo)
add_todo(todo)
add_todo(todo)
write_todo(FILENAME,todo)




