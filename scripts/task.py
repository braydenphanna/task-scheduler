import datetime
from scripts.sort import Sort

class Task:
    def __init__(self, id, name, description, completed, priority, dueDate, creationDate):
        self.id = id
        self.name = name
        self.description = description
        self.completed = completed
        self.priority = priority
        self.dueDate = dueDate
        self.creationDate = creationDate

    def __str__(self):
        s = f"""{"▗▄▖" if self.completed else "┌─┐"} \x1B[1m{self.name}\x1B[0m: {self.description}
{"▝▀▘" if self.completed else "└─┘"} \x1B[2m{self.dueDate.strftime("%#m/%#d/%y, %#I:%M %p")}\x1B[0m"""
        return s

    def contains(self, query):
        return query in self.name or query in self.description

    @classmethod
    def from_csv(cls, line):
        values = line.split(",")
        # helpful datetime formatting cheat sheet: https://strftime.org/
        due_date = datetime.datetime.strptime(values[5], "%m/%d/%y %I:%M %p")
        creation_date = datetime.datetime.strptime(values[6], "%m/%d/%y %I:%M %p")
        return cls(values[0], values[1], values[2], "True" == values[3], values[4], due_date, creation_date)
    
    def compare(self, task, by=Sort.By.NAME):
        if by == Sort.By.NAME:
            return self.name < task.name
        elif by == Sort.By.DUE_DATE:
            return self.dueDate < task.dueDate
        elif by == Sort.By.CREATION_DATE:
            return self.creationDate < task.creationDate
        elif by == Sort.By.COMPLETED:
            return self.completed > task.completed
        elif by == Sort.By.PRIORITY:
            return self.priority < task.priority
    