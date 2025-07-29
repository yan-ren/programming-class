'''
Exercise:

given marks = {'Alice': 90, 'Bob': 65, 'Eve': 82}
create a new dictionary with only students who scored above 80
'''

marks = {'Alice': 90, 'Bob': 65, 'Eve': 82}
new_marks = {}

for name, mark in marks.items():
    if mark > 80:
        new_marks[name] = mark

print(new_marks)

'''
marks = {'Alice': 90, 'Bob': 65, 'Eve': 82, 'Tom': 90}

create a new dictionary by revert the key and value

marks = {90: 'Alice', 65: 'Bob', 82: 'Eve'}
'''

# name1 = 'Alice'
# name2 = 'Tom'
# print(name1 > name2)

# new_marks = {}
#
# for name, mark in marks.items():
#     new_marks[mark] = name

'''
Given a dictionary where values may be duplicated, create a new dictionary that maps each value to a list of keys that had that value
input_dict = {
    'a': 1,
    'b': 2,
    'c': 1,
    'd': 3,
    'e': 2
}

output_dict = {
    1: ['a', 'c'],
    2: ['b', 'e'],
    3: ['d']
}
'''

input_dict = {
    'a': 1,
    'b': 2,
    'c': 1,
    'd': 3,
    'e': 2
}

# output_dict = {}
#
# for k, v in input_dict.items():
#     if v in output_dict:
#         output_dict[v].append(k)
#     else:
#         output_dict[v] = [k]
#
# print(output_dict)

'''
function: packing code as a component
'''
# def welcome():
#     print('Hello')
#     print('Welcome to the class')


# def welcome(name):
#     print('Welcome', name)


# welcome('Tom')
# welcome('Terry')
# welcome()
# def add(a, b):
#     print(a + b)
#
# add(1, 2)

# def calculate(a, b):
#     result = (a + b) * 10
#     return result
#
# print(calculate(1, 2))

# create a function which takes a list of numbers, find the max number and return from the list
# def sum(numbers):
#     max = numbers[0]
#     for value in numbers:
#         if value > max:
#             max = value
#
#     return max
#
# def compare(a, b):
#     if a > b:
#         return True
#     return False

'''
exercise 1:
write a function which takes two list of numbers, return True, if there are common value between the list, otherwise return False

exercise 2:
write a function which takes a list of numbers, return the count of positive number
'''
