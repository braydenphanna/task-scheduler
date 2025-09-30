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
        pass


