from pynput import keyboard
from ui.date_selector import DateSelector
from scripts.task import Task

class GetTask:
    def start(id): 
        name = input("Name: ")
        description = input("Description: ")
        print("Due date: ")
        date = DateSelector.start()
        return Task(id, name, description, False, 1, date)

