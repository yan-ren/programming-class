# a = 1
# b = "text"
#
# if a > 2:
#     print('a is bigger than 2')
# else:
#     print('a is not bigger than 2')

# loops
# while loop almost can be used in everywhere
# for loop need to use together with other thing, e.g. string, list

# example1, loop through each character in the string
# text = "abcdef"
# index = 0
# while index < len(text):
#     print(text[index])
#     index += 1
#
# for i in text:
#     print(i)

# example2, list
# list = []
# list.append(2)
# list.append(3)
# print(list)

# exercise
# using loop to create a list has value [10, 20, 30, 40, ... , 100]
# or [100, 90, 80, ... , 20, 10]
# index = 10
# result = []
# while index <= 100:
#     result.append(result)
#     index += 10

# result = []
# for i in range(10, 101, 10):
#     result.append(i)

# function
def welcome(name, msg):
    print("hello, " + name + ", " + msg)


# welcome("Gilbert", "programming class")

def square(a):
    return a*a


print(square(2))

# write a function that takes a string as input
# and return the same string with the first letter capitalized
# hello -> Hello
# hELlo -> Hello
# HELLO -> Hello
def capitalize(str):
    return str.upper()[0:1] + str.lower()[1:]


# write function takes two input a, b, return the value (a to the power of b)
# def power(a, b):
#     return a ** b
def power(a, b):
    for i in range(b):
        a = a * b
    return a

# call one function inside another function
def a():
    print("a")


def b():
    a()
    print("b")

# escape character, disable the special meaning of symbols
# s = "he said: \"welcome\""
# print(s)

# homework
# write a python function takes two list as input, check if one list contains another list
# [1, 2, 3] [1, 2] -> true
# [1] [1, 2, 3] -> true
# [1, 2] [1, 3] -> false

# write a function, that takes a list of lists, return the list whose length is the largest
# [[1, 2, 3], [1], [2, 4]]

# write a function, that takes a list of lists, return both the longest and shortest list
# [[1, 2, 3], [1], [2, 4]] -> [1, 2, 3], [1]
def min_max_list(lists):
    min = lists[0]
    max = lists[0]

    for list in lists:
        if len(list) > max:
            max = list
        if len(list) < min:
            min = list
    return min, max

# escape character make symbol has no special meaning, just a plan symbol
# escape character disable the special character

s = "hello hello"
s_new = s.replace("llo", "y")
print(s_new)
print(s.isalpha())

# write a function that can do capitalize
# bill's -> Bill's
# hello -> Hello
# HeLLO -> Hello
# hint: str.upper() str.lower() string slicing
def capitalize(str):
    return str.upper()[0] + str.lower()[1:]


s = "    hello   "
print(s)
print(s.strip())
s = "www.google.com"
print(s.strip('w.m'))