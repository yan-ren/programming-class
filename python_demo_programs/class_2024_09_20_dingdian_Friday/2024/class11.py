'''
Python has built-in data structure
'''

l = []
l.append(2)
l.append(3)

print(len(l))
print(l)

'''Given a list of numbers, 
create a new list only with the positive numbers from the original list
hint: use loop and append

given: [1, 2, -1, 4, -3]
new: [1, 2, 4]
'''
# numbers = [1, 2, -1, 4, -3]
# new_numbers = []
#
# for num in numbers:
#     if num > 0:
#         new_numbers.append(num)
#
# print(new_numbers)

text = ['abc', 'ab', 'hello', 'a']

# write a python program to count the number of string where the string length
# is 2 or more
# above example: output = 3
# count = 0
#
# for s in text:
#     if len(s) > 2:
#         count += 1

'''
Given a list of number and a target number, find how many target number exists in the list
example:
number = [1, 2, 1, 2, 4, 1]
target = 1

output = 3
'''
# number = [1, 2, 1, 2, 4, 1]
# target = 1
# count = 0
#
# for num in number:
#     if num == target:
#         count += 1
#
# print(count)

# numbers = [[1, 2, 3], [1, 2, 3]]
# sum = 0
#
# for n in numbers:
#     for num in n:
#         sum += num
#
# print(sum)

'''
Write a program that takes numbers from user, until user type 'finish'
when user type finish, print how many number user has entered and the sum of all numbers
using list
'''
numbers = []

while True:
    value = input('Enter a number or finish')

    if value == 'finish':
        break
    else:
        numbers.append(int(value))

# calculate sum and len()


'''
Homework:
Given a list, reverse it

e.g.
list = [1, 2, 1, 4]
expect:
[4, 1, 2, 1]
'''