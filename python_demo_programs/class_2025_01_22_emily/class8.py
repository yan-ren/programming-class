# 2D list
# matrix = [[1, 2, 3],
#           [2, 3, 4],
#           [4, 5, 6]]
#
# # nested loop
# s = 0
# for row in matrix:
#     for col in row:
#         # s += col
#         print(col)
#
# print(s)
# print(matrix[1][2])

# def print_message():
#     print('Welcome to the class')
#     print('Today is a good day')

# print_message()
# print_message()
# print_message()

# def welcome(name):
#     print('Welcome', name)

# welcome('Tom')
# welcome('Jerry')
# welcome('Tom', 'Jerry') # wrong: pass more value that function receives
# welcome()   # wrong: pass zero to a function that is looking for one value

# def add(a, b):
#     c = a + b
#     return c
#
# # return has two features, 1. terminate the function, 2, return the value
# def division(a, b):
#     if b == 0:
#         return
#     c = a / b
#     return c
#
#
# res = add(1, 2)
# print(res)
# res = division(1, 0)
# print(res)

def max_min_value(numbers):
    max = numbers[0]
    min = numbers[0]
    for value in numbers:
        if value > max:
            max = value
        if value < min:
            min = value

    return max, min

a, b = max_min_value([1, 2, 1, 4, 2, 5])
print(a)
print(b)
# print(max_min_value([1, 2, 1, 4, 2, 5]))
# print(max_min_value([10, 20, 1, 4, 2, 5]))

def add(a, b):
    c = a + b
    return c

print(add(1, 2))
#     sub(c)
#
# def sub(a):
#     a = a - 1
#     print(a)
#
# add(1, 2)

# [1, 2, 1, 3, 2] -> [1, 2, 3]
def unique(numbers):
    new_numbers = []

    for v in numbers:
        if v not in new_numbers:
            new_numbers.append(v)

    return new_numbers

print(unique([1, 2, 1, 3, 2]))

def count(list, target):
    counter = 0
    for value in list:
        if value == target:
            counter += 1

    return counter

print(count([1, 2, 3, 1], 1))

def count_consonant(s):
    vowels = 'aeiou'
    count = 0

    for letter in s:
        if letter not in vowels:
            count += 1

    return count

# given a list of number, count how many positive value
# e.g. [1, 2, -1, 2, -3] -> 3

