from scripts.task import Task

class Search:
    # returns single task
    # only works for IDs 
    def binary(tasks, query):
        mid = int(len(tasks)/2)
        if len(tasks) == 1 and not tasks[mid].contains(query):
            return 
        elif tasks[mid].id == query: 
            return tasks[mid]
        elif tasks[mid].id < query:
            return Search.binary(tasks[mid:],query)
        elif tasks[mid].id >query:
            return Search.binary(tasks[:mid],query)
  
    # returns multiple tasks
    def linear(tasks, query):
        results = []
        for task in tasks:
            if (task.contains(query)):
                results.append(task)
        return results