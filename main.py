from scripts.task import Task
from scripts.sort import Sort
from scripts.search import Search
import datetime

tasks = []

with open("data_set.csv") as f:
    for line in f.read().splitlines()[1:]: # removes first row of file
        #print(Task.from_csv(line))
        tasks.append(Task.from_csv(line))

tasks = Sort.heap(tasks, Sort.By.NAME)

tasks = Search.linear(tasks, "name")

for task in tasks:
    print(task)
