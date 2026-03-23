'''
review python list
knowledge path
project path
'''
# name = ['Alice', 'Bob', 'Charles', 'Alice']
# print(len(name))

# # access the element by index, 0, 1, 2, ...
# print(name[0])
#
# for n in name:
#     print(n)
#
# # check for existence
# # if 'Tom' in name:
#
# name.append('Tom')
# print(name)
#
# name.insert(0, 'Jerry')
# print(name)

# name.remove('Alice# name = ['Alice', 'Bob', 'Charles', 'Alice']

# if you have multiple value, how does remove work?
# answer: only the first value from the left being removed

# to remove all values
# while 'Alice' in name:
#     name.remove('Alice')

name = ['Alice', 'Bob', 'Charles', 'Alice']
# how to create a new reversed list
# e.g. ['Alice', 'Charles', 'Bob', 'Alice']
name_reversed = []

for n in name:
    name_reversed.insert(0, n)

print(name_reversed)

numbers = [[1, 2, 3], [2, 3], [3, 5]]
# when you have a 2d list, how to loop through all values?
# using 2 loops
for sub in numbers:
    for num in sub:
        print(num)

# homework: given a 2d list of numbers, calculate the sum of all numbers
# e.g. numbers = [[1, 2, 3], [2, 3], [3, 5]]
# answer: 19

numbers = [[1, 2, 3], [2, 3], [3, 5]]
sum = 0
for sub in numbers:
    for num in sub:
        sum += num

print(sum)