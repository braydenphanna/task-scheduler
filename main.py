from scripts.task import Task
from scripts.sort import Sort
from ui.search import Search
from ui.add_task import AddTask
import datetime
import sys

tasks = []

with open("data_set.csv") as f:
    for line in f.read().splitlines()[1:]: # removes first row of file
        tasks.append(Task.from_csv(line))

tasks = Sort.merge(tasks, Sort.By.DUE_DATE)

if (("-h" or "--help") in sys.argv):
    print("Usage:\n python3 ./main.py [options]\n")
    print("Options:")
    print(" -a, --add\tadd a task")
    print("\n -h, --help\tdisplay this help")
elif (("-a" or "--add") in sys.argv):
    AddTask.start()
elif (("-s" or "--search") in sys.argv):
    Search.start(tasks)


# for task in tasks:
#    print(task)