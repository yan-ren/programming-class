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
# a = [1, 2, [3, 4]]
# b = [[5, 6], [7, 8]]
# # for each value in a, combine with each value in b to a new list
# # output
# [[1, 5, 6], [1, 7, 8], [2, 5, 6], [2, 5, 6], [3, 4, 5, 6], [3, 4, 7, 8]]
#
# def merge(a, b):
#     res = []
#     for i in a:
#         for j in b:
#             tmp = []
#             if type(i) is list:
#                 tmp.extend(i)
#             else:
#                 tmp.append(i)
#             if type(j) is list:
#                 tmp.extend(j)
#             else:
#                 tmp.append(j)
#             res.append(tmp)
#     return res
# print(merge(a, b))

# given a list of numbers, write a function that returns a new list with only odd numbers and bigger than 5
# input: [1, 2, 4, 5, 6, 7, 9]
# return: [7, 9]

# def filter(input):
#     result = []
#     for i in input:
#         if i % 2 != 0 and i > 5:
#             result.append(i)
#     return result
#
# # print(filter([1, 2, 4, 5, 6, 7, 9]))
#
# print("doesn't")
# # backslash is a special character that tells python the character
# # followed it is just a text character
# # escape character
# print('doesn\'t')
#
# s = "hello"
# for i in s:
#     print(i)


# next class: more about string
# homework: function Q9

# s = [4, 2, 5, 1]
#
# def odd_index(input):
#     # while loop go through each value in list
#     # check index even or odd
#     index = 0
#     result = []
#     while index < len(input):
#         if index % 2 == 1:
#             result.append(input[index])
#         index += 1
#     return result

# greeting = 'Hello World, Hello!'
#
# print(greeting.find('ll'))
# print(greeting.replace('llo', 'y'))
# print(greeting)
# print(greeting.startswith('Ha'))
# print(greeting.lower())
# print(greeting)
# print(greeting.upper())
# print(greeting)

# given a list of numbers, calculate the average of list
# largest index = length - 1
a = [1, 2, 3, 4]

# factorial is a math calculation 5! = 5 * 4 * 3 * 2 * 1
# 3! = 6
# write a function calculates the factorial of a number n!
# def factorial(n):
#     result = 1
#     for i in range(1, n+1):
#         result = result * i
#     return result
# factorial(10)

# write a function takes two inputs, first input is a number, second input is a list
# part1: function should tell you how many numbers found in the list
# a = 1, b = [1, 1, 1, 1]
# part2: find the highest frequency number in the list, part2 will use the function written in part1
b = [1, 1, 2, 2, 3, 3, 3]
def counter(target, source):
    count = 0
    for i in source:
        if target == i:
            count += 1
    return count


def highest_freq(source):
    highest_number = 0
    freq = 0
    for i in source:
        if counter(i, source) > freq:
            highest_number = i
            freq = counter(i, source)

    return highest_number

# greeting = "Hello hi"
# print(greeting.lower())
# print(greeting)
# print(greeting.upper())
# print(greeting.upper())
#
# greeting = "    Hello   ?   "
# print(greeting)
# print(greeting.strip())

# given = '  hello  ?  '
# # how do I get 'hello'
# print(given.strip(' ?'))
# a = 'abc'
# b = [1, 2, 3]

# write a function that takes a string and returns a list
# input: 'abc'
# output: ['a', 'b', 'c']
# def string_to_list(str):
#     result = []
#     for i in str:
#         result.append(i)
#     return result
#
#
# def list_to_string(list):
#     result = ''
#     for i in list:
#         result += i
#     return result
#
# test = ' Ham,Cheese,Bacon?'
# # want a list ['ham', 'chesse', 'bacon']
# print(test.strip(' ?').lower().split(','))
# test = test.strip(' ?')
# test = test.lower()
# print(test.split(','))
# write a function that takes a string and returns a list
# input: 'abcd'
# output: ['a', 'b', 'c', 'd']


# # empty string
# s = ''
# # empty list
# l = ['']

# write a function that takes a list and returns a string
# input: ['s', 'b', 'c']
# output: 'sbc'

# date = '2020-02-02'
# result = date.split('-')
# print(type(result))
# print(result)


# write a function that takes two string in date format, e.g '2020-02-20', '2012-02-12'
# compare which date is earlier

# start comparison with year
# when year is equal continue with month then day
def compare_date(date1, date2):
    date1 = date1.split('-')
    date2 = date2.split('-')

    # compare the year
    if int(date1[0]) != int(date2[0]):
        if int(date1[0]) < int(date2[0]):
            print('date1 is earlier')
        else:
            print('date2 is earlier')
    # compare the month
    elif int(date1[1]) != int(date2[1]):
        if int(date1[1]) < int(date2[1]):
            print('date1 is earlier')
        else:
            print('date2 is earlier')
    # compare the day
    elif int(date1[2]) != int(date2[2]):
        if int(date1[2]) < int(date2[2]):
            print('date1 is earlier')
        else:
            print('date2 is earlier')
    else:
        print('two dates are equal')
#
# # compare_date('2020-02-03', '2020-01-05')
# list = ['Eric', 'John', 'Michael']
# result = ''.join(list)
# print(result)

# a = '{} is equal to {}'
# b = a.format('hello', 'hi')
# print(a)
# print(b)
# print("{0} can be {1} {0}s".format("strings", "formatted"))

# homework: jacky read slides 1.1 page 103-119

# def odd_index(input):
#     index = 0
#     res = []
#     while index < len(input):
#         if index % 2 == 1:
#             res.append(input[index])
#         index += 1
#
#     return res


# def odd_index(input):
#     index = 0
#     res = []
#     for i in input:
#         if index % 2 == 1:
#             res.append(i)
#         index += 1
#
#     return res
#
# print(odd_index([1, 2, 3, 4, 5]))

# def find_largest(list):
#     # largest = list[0]
#     # for i in list:
#     #     if largest < i:
#     #         largest = i
#     # return largest
#     index = 0
#     largest = list[index]
#     while index < len(list):
#         if list[index] > largest:
#             largest = list[index]
#         index += 1
#     return largest
#
#
# def find_second_largest(list):
#     largest = find_largest(list)
#     list.remove(largest)
#     return find_largest(list)
#
#
# print(find_second_largest([1, 2, 3, 4, 5]))

# list = [0, 10, 20, 30]
# i = 0
# while i < len(list):
#     print(list[i])
#     i += 1
#
# # in keywords -> iterable: string, list
# for i in range(4):
#     print(i)

# range(4) -> [0, 1, 2, 3]


# print even numbers between r1 to r2
# r1 = int(input("Enter the starting range value?"))
# r2 = int(input("Enter the ending range value?"))
#
# print("Range: %d - %d" % (r1, r2))
#
# num = r1 + 1
# count = 0
#
# while num < r2:
#     print("num: %d" % (num))
#     res = num % 2
#     print("res: %d" % (res))
#     if (num % 2) > 0:
#         count += 1
#     num += 1
#
# print("Odd count: %d" % (count))

# write a function that takes a number between 0-100.
# if you enter a valid number 5 times, then the function finish
# otherwise print message

def valid_input():
    chance = 5
    while chance > 0:
        number = int(input('enter a number:'))
        if 0 < number < 100:
            return 'valid input'
        else:
            chance -= 1

    return 'input failed'

# print the following pattern
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# question 1, write a function takes one input as pattern and print the pattern triangle
def pattern_print(pattern, line):
    row = 1
    while row <= line:
        column = 1
        while column <= row:
            print(pattern, end=' ')
            column += 1
        print()
        row += 1

# pattern_print('@', 3)


# write a function takes a string as input, return a reversed string
# input: 'abcd'
# output: 'dcba'

def reverse(string):
    res = ''
    index = len(string) - 1
    while index >= 0:
        res = res + string[index]
        index -= 1
    return res

# write a function to reverse a list in place without creating new list/slicing
# [1, 2, 3, 4, 5]
# use switching, e.g. first element switches with last element
# second element switches with second last element. so on.
def reverse_list(list):
    index = 0
    while index < len(list) / 2:
        tmp = list[index]
        list[index] = list[len(list) - 1 - index]
        list[len(list) - 1 - index] = tmp
        index += 1

    return list
# string is immutable - cannot change values after created
# list is mutable - can change values after created

# write a function takes a list of numbers(positive/negative)
# if the number is positive, leave it unchanged
# if the number is negative, reserved it
# then return the positive sum

# if the number is positvie, reserved it
# if the number is negative, leave it unchanged
# def sum(list):
#     res = 0
#     for i in list:
#         if i > 0:
#             res += i
#         else:
#             res += -1 * i
#     return res

# write a function takes a list of lists, all values in the inner list are number
# calculate the sum of all numbers
# [[1, 2, 3], [1, 2]]
# 9

# try to loop a list of numbers, positive, negative, return the first negative from the left
# [1, -2, -3, -4]
# 1 + 2 + 3 + 4

# [1, 2, 3, 4]

# homework, write the same program again
# write a function takes a list of numbers, positive and negative, sum all the positive numbers
# and return the sum
# [1, 2, -3]
# 3

# write a function, check if a list has negative number if has, return false, else return true
# [1, 2, 3]
def check_positive(list):
    for i in list:
        if i < 0:
            return False

    return True


def check_positive(list):
    result = True
    for i in list:
        if i < 0:
            result = False
            break
    return result

# def multiple_return(list):
#     a = None
#     b = None
#     for i in list:
#         if i > 0 and a is None:
#             a = i
#         if i < 0 and b is None:
#             b = i
#     return a, b

# [1, 2, 4, 1]
# return 1, None

# break & continue
# two keywords used in loop(for loop, while loop)
# break: breaks the loop
# continue: stop the current cycle, continue with next cycle


# range(10) -> [0, 1, 2, ..., 9]



# in other programming languages, sometime we can only return one value from function
# but in python, we can return multiple values at the same time
# def multiple_return():
#     a = 1
#     b = 2
#     return a, b
#
# print(multiple_return())
# a, b = multiple_return()
# print(a)
# print(b)

#return the sum of all positives and sum of all negatives
# [1, 2, -1, -2]
# return 3, -3

# homework
# write a function takes a list, all number in list are positive
# return the sum of all even numbers and all odd numbers
# [1, 2, 4, 2, 3]
# return 8, 4


# write a function takes two lists as input, return the number of positive numbers and negative number in two lists
# example: list1=[1, 2, -1], list2=[2, -3]
# return 3, 2
# def positive_negative(list1, list2):
#     n_positive = 0
#     n_negative = 0
#     list1.extend(list2)
#     for i in list1:
#         if i > 0:
#             n_positive += 1
#         else:
#             n_negative += 1
#
#     return n_positive, n_negative
#
#
# a = [1, 2, 3, 3, 3]
# print(a.count(9))

# write a function that removes the duplicate in the list
# def remove_duplicate(list):
#     index = 0
#     while index < len(list):
#         j = index + 1
#         while j < len(list):
#             if list[index] == list[j]:
#                 del list[j]
#                 j -= 1
#             j += 1
#         index += 1
#     return list


