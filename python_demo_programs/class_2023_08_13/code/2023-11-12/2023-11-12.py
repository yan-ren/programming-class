from queue import PriorityQueue

q = PriorityQueue()
# q.put(4)
# q.put(2)
# q.put(1)
# q.put(5)
# q.put('abcd')
# q.put('aa')
# q.put('bb')

q.put((4, 'Tom'))
q.put((2, 'Jerry'))
q.put((5, 'Micky'))
q.put((1, 'Mike'))
q.put((1, 'Make'))

while not q.empty():
    print(q.get())