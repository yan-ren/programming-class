'''
given two lists of numbers, combine them together by removing the duplicates

a = [1, 2, 3]
b = [2, 3, 5]

c = [1, 2, 3, 5]
'''
# a = [1, 2, 3]
# b = [2, 3, 5]
#
# result = []
# for value in a:
#     if value not in result:
#         result.append(value)
#
# for value in b:
#     if value not in result:
#         result.append(value)

# l = [[3, 4], [1, 2]]
#
# for v in l:
#     for num in v:
#         print(num)

'''
write a program that takes a 2d list of integers, return a list where each element is the largest number
from the corresponding row of the 2d list

matrix = [
    [3, 5, 9],
    [1, 7, 4],
    [2, 8, 6]
]

result = [9, 7, 8]
'''

# function
def find_max(numbers):
    max = numbers[0]
    for v in numbers:
        if v > max:
            max = v

    return max


def add(a, b):
    return a+b


n = [1, 2, 3, 4]
print(find_max(n))
n = [1, 2, 3, 4, 5]
print(find_max(n))
print(add(1, 2))

'''
write a function to check if a list has a duplicated value or not
e.g. [1, 2, 1] -> True
[1, 2] -> False
'''
def check_duplicate(l):
    seen = []

    for value in l:
        if value not in seen:
            seen.append(value)
        else:
            return True

    return False


def welcome():
    print('hello')


welcome()
welcome()

def math_operation(a, b):
    # return a + b, a * b, a - b
    if b == 0:
        return

    return a + b, a / b


# print(math_operation(1, 2))
# a = math_operation(1, 2)
# print(a)
# print(b)
'''
Write a python function that takes two lists as input
check if they have value in common
'''

# def find_common(list1, list2):

