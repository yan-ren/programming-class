import heapq
from queue import PriorityQueue

'''
helper lib
'''
customers = []
# # heapq pushes item (2, 'Harry') into the list, where the first value 2 is the priority, and 'Harry'
heapq.heappush(customers, [2, 'Harry'])
heapq.heappush(customers, (3, 'Charles'))
heapq.heappush(customers, (4, 'Jerry'))
#
# while customers:
#     print(heapq.heappop(customers))

customers = PriorityQueue()

customers.put((2, 'Harry'))
customers.put((3, 'Charles'))
customers.put((1, 'Jerry'))

while customers:
    print(customers.get())

