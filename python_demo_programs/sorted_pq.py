from operator import attrgetter


class SortedPriorityQueue:
    class Node:
        def __init__(self, value, priority):
            self.value = value
            self.priority = priority
        
        def __str__(self):
            return str(self.value) + ":" + str(self.priority)
    
    def __init__(self):
        self.data = []

    def add(self, value, priority):
        self.data.append(self.Node(value, priority))
        # sort list by proirty
        self.data.sort(key=attrgetter('priority') )

    def remove():
        pass


queue = SortedPriorityQueue()
queue.add('a', 2)
queue.add('b', 1)
for data in queue.data:
    print(data)


# class Car:
#     def __init__(self, name):
#         self.name = name

#     def __str__(self):
#         return self.name


# car = Car('toyota')
# print(car)
