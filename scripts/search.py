from scripts.task import Task

class Search:
    # returns single task
    def binary(tasks, query):
        pass

    # returns multiple tasks
    def linear(tasks, query):
        results = []
        for task in tasks:
            if (task.contains(query)):
                results.append(task)
        return results