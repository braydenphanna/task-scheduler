# task-scheduler
## Roadmap

- [ ] **Collect Data**
    - Create a seperate program to generate data of X size
- [ ] **Create a class named `Task`**
    - Has a `name` string
    - Has a `description` string
    - Has a `completed` boolean
    - Has a `priority` integer (1->3 or 1->5)
    - Has a `dueDate` date and time
    - Has a `creationDate` date and time
    - Has a `toString` function that prints it all nicely
- [ ] **Command line interface** (Work in progress)
    - `-d` or `--daily`: print daily task list
    - `-e` or `--export`: export task list as `.csv`
    - `-i` or `--import`: import task list as `.csv`
