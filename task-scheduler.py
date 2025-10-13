#!/usr/bin/env python3

from scripts.task import Task
from scripts.sort import Sort
from scripts.task_knn import suggested_tasks
from scripts.generate_data import generate
from scripts.emails import send_email
from ui.search import Search
from ui.get_task import GetTask
from datetime import datetime
import sys

tasks = []

BOLD="\x1b[1m"
END_BOLD="\x1b[22m"
GREEN="\x1b[32m"
END_GREEN="\x1b[39m"

with open("data_set.csv") as f:
    for line in f.read().splitlines()[1:]: # removes first row of file
        tasks.append(Task.from_csv(line))

tasks = Sort.merge(tasks, Sort.By.DUE_DATE)

if ("-a" in sys.argv or "--add" in sys.argv):
    task = GetTask.start(len(tasks))
    tasks.append(task)
    with open("data_set.csv", "a") as f:
        f.write(task.to_csv())
elif ("-g" in sys.argv or "--generate" in sys.argv):
    generate()
elif ("-s" in sys.argv or "--search" in sys.argv):
    Search.start(tasks)
elif ("-d" in sys.argv or "--daily" in sys.argv):
    Search.start(list(filter(lambda t: t.due_date.date() == datetime.today().date(), tasks)))
elif ("-r" in sys.argv or "--recommend" in sys.argv):
    suggested_tasks()
elif ("-m" in sys.argv or "--mail" in sys.argv):
    email = input("Enter your email: ")
    send_email(email)
else:
    print(f"\n{BOLD}Usage:{END_BOLD}\n {GREEN}./task-scheduler.py{END_GREEN} [option]\n")
    print(f"{BOLD}Options:{END_BOLD}")
    print(" -a, --add      \tadd a task")
    print(" -d, --daily    \tfetch daily tasks")
    print(" -g, --generate \tgenerate fake tasks")
    print(" -m, --mail     \temail daily tasks")
    print(" -r, --recommend\trecommend tasks")
    print(" -s, --search   \tsearch tasks")
    print("\n -h, --help   \t\tdisplay this help\n")


    # 
