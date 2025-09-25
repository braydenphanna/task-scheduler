import datetime

class Task:
    def __init__(self, name, description, completed, priority, dueDate, creationDate):
        self.name = name
        self.description = description
        self.completed = completed
        self.priority = priority
        self.dueDate = dueDate
        self.creationDate = creationDate

    def __str__(self):
        s = f"""{"▗▄▖" if self.completed else "┌─┐"} \x1B[1m{self.name}\x1B[0m: {self.description}
{"▝▀▘" if self.completed else "└─┘"} \x1B[2m{self.dueDate.strftime("%-m/%-d/%y, %-I:%M %p")}\x1B[0m"""
        return s

task1 = Task("Eat breakfast", "Eat 3 eggs and drink milk", True, 1, datetime.datetime(2025, 9, 25, 8), datetime.datetime.now())
task2 = Task("Add sorting to program", "Code merge sort", False, 1, datetime.datetime(2025, 9, 25, 12), datetime.datetime.now())
task3 = Task("Sleep", "Lay in bed", False, 1, datetime.datetime(2025, 9, 25, 23), datetime.datetime.now())
print(task1)
print(task2)
print(task3)