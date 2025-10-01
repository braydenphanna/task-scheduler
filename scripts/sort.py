import math
from enum import Enum

class Sort:
    class By(Enum):
        NAME = 1
        DUE_DATE = 2
        CREATION_DATE = 3
        COMPLETED = 4
        PRIORITY = 5
        
    def quick(tasks, by):
        pass

    def merge(tasks, by):
        if len(tasks) <= 1:
            return tasks
        
        mid = int(len(tasks)/2)
        left = tasks[:mid]
        right = tasks[mid:]

        lSorted = Sort.merge(left, by)
        rSorted = Sort.merge(right, by)

        return Sort.__merger(lSorted, rSorted, by)

    def __merger(left, right, by):
        merged = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i].compare(right[j], by):
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        merged.extend(left[i:])
        merged.extend(right[j:])

        return merged

    def heap(tasks, by):
        start = math.floor(len(tasks) / 2)
        end = len(tasks)
        while (end > 1):
            if (start > 0):
                start -= 1
            else:
                end -= 1
                Sort.__swap(tasks, end, 0)
            Sort.__sink(tasks, start, end, by)
        return tasks

    def __sink(tasks, root, end, by):
        while 2 * root + 1 < end:
            child = 2 * root + 1
            if child + 1 < end and tasks[child].compare(tasks[child + 1], by):
                child += 1
            if tasks[root].compare(tasks[child], by):
                Sort.__swap(tasks, root, child)
                root = child
            else:
                break

    def __swap(list, a, b):
        list[a], list[b] = list[b], list[a]