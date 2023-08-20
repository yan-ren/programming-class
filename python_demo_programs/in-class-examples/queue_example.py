# q = []
# q.append(1)
# q.append(2)
# q.append(3)
#
# # stack
# print(q.pop())
# print(q)
#
# # queue
# print(q.pop(0))
# # q[0]
# print(q)

from queue import Queue

# q = Queue()
# print(type(q))
# q.put(1)
# q.put(2)
# print(q.queue)
# print(q.get())
# print(q.qsize())
# print(q.empty())

'''
Your task is to construct a tower in N days by following conditions:
- every day you are provided with one disk of distinct size
- the disk with larger size should be placed at the bottom of the tower
- the disk with smaller sizes should be placed at the top of the tower
Output
print N lines. in the ith line, print the size of disks that can be placed on the top of the tower in descending order 
of the disk sizes

sample input:
5
4 5 1 2 3

print
[[4,5], [1,2,3]]


'''
# input = [2, 8, 9, 1, 3, 2, 6]
# result = []
# start_index = 0

# while start_index < len(input):
#     end_index = start_index + 1
#     while end_index < len(input) and input[end_index] > input[end_index-1]:
#         end_index+=1
#     if end_index - start_index > 1:
#         result.append(input[start_index:end_index])
#         start_index = end_index

# print(result)

'''
given a list of numbers, remove all zeros from the list(move zeros to the end), without creating new list

[2, 0, 3, 0, 1, 9]
position = 0
loop from i : 0 to end of the list
[2, 0, 3, 0, 1, 9]
position = 1
i = 2
[2, 3, 0, 0, 1, 9]
position = 2
[2, 3, 1, 0, 0, 9]
position = 3


'''
# a = 1
# b = 2
# a, b = b, a

# print(a, b)

# # implement queue using list
# queue = []

# # adding elements to the queue
# queue.append(1)
# queue.append(2)

# # list method: remove index 0 == remove elements from the queue
# print(queue.pop(0))
# print(queue.pop(0))


'''
given a list of numbers and int k, calculate the moving average for every k elements

e.g. [2, 3, 4, 1, 5, 2, 1]

k = 2

[2.5, 3.5, 2.5, 3, 3.5, 1.5]
'''
src = [2, 3, 4, 1, 5, 2, 1]
k = 2
res = []
q = Queue()

for i in src:
    q.put(i)
    if q.qsize() == k:
        res.append(sum(list(q.queue)) / k)
        q.get()


print(res)