from pynput import keyboard
from ui.date_selector import DateSelector
from scripts.task import Task

class AddTask:
    name = ""
    description = ""
    date = ""

    def start():
        Task(0, AddTask.name, AddTask.description, False, 1, AddTask.date)
        AddTask.name = input("Name: ")
        AddTask.description = input("Description: ")
        print("Due date: ")
        DateSelector.start()

    def __on_press(key):
        pass

