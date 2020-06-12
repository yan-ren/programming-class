# # a^b
# def power(a, b):
#     res = 1
#     for i in range(b):
#         res = res * a
#     return res
#
# print(power(2, 3))
# # 2^3 = 2*2*2
#
#
# # 2^3 = 2 * (2^2)
# def recursive_power(a, b):
#     if b == 0:
#         return 1
#     return a * recursive_power(a, b - 1)
#
# # 2^3 = 2 * (2^2) = 2 * 2 * 2^1 = 2 * 2 * 2 * 2^0


# a = [[1,2,3], [4,5,6], [10,11,12], [7,8,9]]

# given a list, calculate the sum for a list
# def sum_list(l):
#     sum = 0
#     for i in l:
#         sum += i
#     return sum
#
# # give a list of lists, loop through each sublist, call the sum_list function, calculate sum if the sum
# # is the largest, remember the largest and the list
#
# def largest_sublist(l):
#     # i is a list
#     largest = 0
#     largest_sublist = []
#     for i in l:
#         temp = sum_list(i)
#         if temp > largest:
#             largest = temp
#             largest_sublist = i
#
#     return largest_sublist


# homework
# write a function, given a list, return the largest value in the list
# example input [10, 20, 30, 40]
# return 40

# def cal_upper_lower(input):
#     upper = 0
#     lower = 0
#     for i in input:
#         if 'A' <= i <= 'Z':
#             upper += 1
#         elif 'a' <= i <= 'z':
#             lower += 1
#     print('upper case:', upper)
#     print('lower case:', lower)
#
#
# a = "This is a STRING"
# cal_upper_lower(a)

# write a function, takes a list as input, then return the minimum value in the list
# assume list has all numbers
# [3, 2, 1]
#

# write a function, takes a list as input, then return the sum of all values in the list

# write a function, takes a list as input, then return the product of all values in the list

# write a function, takes a list as input, return a list that has only even numbers
# inside function, create a new list, loop through input list, if find an even number,
# put the number in the new list

# write a function, takes a string as input, return a number,
# this number represents how many space in the string
# input: "This is a string"
# return: 3

# def unique(input):
#     result = []
#     for i in input:
#         if i not in result:
#             result.append(i)
#
#     return result
#
# print(unique([1, 2, 3, 3, 3]))

# another way: remove the duplicate, don't create new list

# def odd(input):
#     result = []
#     for i in input:
#         if not i % 2 == 0:
#             result.append(i)
#     return result
#
# print(odd([1, 2, 3, 3, 3, 5]))

# def safe_input(min, max):
#     while True:
#         tmp = int(input('enter a number'))
#         print("you entered:", tmp)
#         if min <= tmp <= max:
#             return tmp
#
#
# def safe_input2(values):
#     while True:
#         tmp = input('enter a value')
#         if tmp in values:
#             return tmp
#         else:
#             print('you entered', tmp)
#
#
# safe_input(1, 50)
# safe_input(1, 10)
# safe_input2(["yes", "no"])

# s = "abba"

# input
a = [1, 2, [3, 4]]
b = [[5, 6], [7, 8]]
# for each value in a, combine with each value in b to a new list
# output
[[1, 5, 6], [1, 7, 8], [2, 5, 6], [2, 5, 6], [3, 4, 5, 6], [3, 4, 7, 8]]

def merge(a, b):
    res = []
    for i in a:
        for j in b:
            tmp = []
            if type(i) is list:
                tmp.extend(i)
            else:
                tmp.append(i)
            if type(j) is list:
                tmp.extend(j)
            else:
                tmp.append(j)
            res.append(tmp)
    return res
print(merge(a, b))