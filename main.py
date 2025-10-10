from scripts.task import Task
from scripts.sort import Sort
from scripts.generate_data import generate
from ui.search import Search
from ui.get_task import GetTask
import datetime
import sys

tasks = []

with open("data_set.csv") as f:
    for line in f.read().splitlines()[1:]: # removes first row of file
        tasks.append(Task.from_csv(line))

tasks = Sort.merge(tasks, Sort.By.DUE_DATE)

if ("-h" in sys.argv or "--help" in sys.argv):
    print("Usage:\n python3 ./main.py [options]\n")
    print("Options:")
    print(" -a, --add\tadd a task")
    print(" -g, --generate\tgenerate fake tasks")
    print(" -s, --search\tsearch tasks")
    print("\n -h, --help\tdisplay this help")
elif ("-a" in sys.argv or "--add" in sys.argv):
    task = GetTask.start(len(tasks))
    tasks.append(task)
    with open("data_set.csv", "a") as f:
        f.write(task.to_csv())
elif ("-g" in sys.argv or "--generate" in sys.argv):
    generate()
elif ("-s" in sys.argv or "--search" in sys.argv):
    Search.start(tasks)