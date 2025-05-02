'''
List comprehension
Dictionary comprehension
Set comprehension
'''
'''
Create a list of number like following
[0, 1, 4, 9, 16]

hint: using loop
'''
# numbers = []
# for i in range(5):
#     numbers.append(i**2)

# numbers = [i**2 for i in range(5)]
#
# print(numbers)

'''
Create a list of number in following format
[0, 2, 4, 6, 8]
'''
# even = []
#
# for i in range(10):
#     if i % 2 == 0:
#         even.append(i)
#
# print(even)
#
# even = [i for i in range(10) if i % 2 == 0]

l = [print(i*10, end=' ') for i in range(11)]

l = [i * 10 for i in range(11)]
print(l)