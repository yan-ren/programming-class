'''
function/method
'''

# def list_sum(list):
#     sum = 0
#     for value in list:
#         sum += value
#
#     return sum
#
#
# sum = list_sum([1, 2, 3])
# print(sum)
# list_sum([2, 3, 4])

# def add(a, b):
#     c = a + b
#     return c
#
# print(add(1, 2))

def add_subtract(a, b):
    return a+b, a-b

'''
Write a function that takes a list of number as input
and return the largest in the list
'''
# def max_min(l):
#     max = l[0]
#     min = l[0]
#
#     for value in l:
#         if value > max:
#             max = value
#         if value < min:
#             min = value
#
#     result = []
#     result.append(max)
#     result.append(min)
#     return result

# def input_in_range(message, min, max):
#     # while True:
#     number = int(input(message))
#     if number >= min and number <= max:
#         return number
#     else:
#         print('type again')
#
# n = input_in_range("Enter age:", 0, 100)

# a = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]
#
# def sum_list(list):
#     sum = 0
#     for value in list:
#         sum += value
#     return sum
#
# def sum_matrix(matrix):
#     sum = 0
#     for list in matrix:
#         sum = sum + sum_list(list)
#
#     return sum
#
# print(sum_matrix(a))
#
# def method1(a):
#     print(a)
#     method2(a + 1)
#
# def method2(a):
#     print(a)
#
#
# method1(10)

def count_vowel(s):
    vowel_list = ['a', 'e', 'i', 'o', 'u']
    counter = 0
    for letter in s:
        if letter in vowel_list:
            counter += 1

    return counter


print(count_vowel('hello'))