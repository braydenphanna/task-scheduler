from scripts.task import Task

with open("data_set.csv") as f:
    for line in f.read().splitlines()[1:]: # removes first row of file
        print(Task.from_csv(line))