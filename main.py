from scripts.task import Task
from scripts.sort import Sort
from scripts.search import Search
import datetime
import sys

if (("-h" or "--help") in sys.argv):
    print("Usage:\n python3 ./main.py [options]\n")
    print("Options:")
    print(" -a, --add\tadd a task")
    print("\n -h, --help\tdisplay this help")
elif (("-a" or "--add") in sys.argv):
    name = input("Name: ")
    description = input("Description: ")
    priority = input("Priority (1-5): ")
    due_date = input("Due Date (MM/DD/YY 00:00 AM): ")

tasks = []

with open("data_set.csv") as f:
    for line in f.read().splitlines()[1:]: # removes first row of file
        tasks.append(Task.from_csv(line))

tasks = Sort.heap(tasks, Sort.By.NAME)

# for task in tasks:
#     print(task)
