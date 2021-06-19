'''
global scope: the program runs outside of the function is running on the global scope
global variable: the variable on the global scope

function local scope: every time call a function, program enters the local scope
local variable: the variable on the local scope

default behaviour 1: if program runs on local scope(inside a function), program first search on local scope for variable
if variable not found on local scope, program searches the variable on global scope
rule: a variable cannot be both local and global inside of a function
'''

# def foo():
#     print(s) # print local s, error because cannot find s on local scope
#     s = "Me too." # because of this variable definition, python thinks we want to use local s all the time
#     print(s) # print local s
#
#
# s = "I hate spam."
# foo()
# print(s)

# def foo():
#     global s # use global s inside function
#     print(s) # print global s
#     s = "That's clear." # set global s = “That’s clear”
#     print(s) # print global s
#
#
# s = "Python is great!"
# foo()
# print(s) # ?

def calculation():
    global place
    place = "Cape Town"
    global name # name should be defined on global scope
    name = "John" # global variable "name"

    print(locals())
    print(globals())


place = "Berlin"
print(place)
calculation()
print(name)

'''
write a python function that takes a string and returns a dictionary
the dictionary key is the each character in the string, the value is the frequency of the character

s = "abbc"
d = {"a": 1, "b": 2, "c": 1}

s = "hello"
d = {"h": 1, "e": 1, "l": 2, "o": 1}
'''

'''
about global keyword
global keyword allows you to modify the global variable inside a function
'''

def keys_number(string):
    dic = {}
    for char in string:
        dic[char] = count_char(char, string)
    return dic

# count_char counts how many times the target character is in the source string
def count_char(target, source):
    counter = 0
    for j in source:
        if target == j:
            counter += 1
    return counter


print(keys_number('12215'))

'''
Write a Python program to print a dictionary where the keys are numbers between 1 and 10 (both included) 
and the values are square of keys. Solve this problem using dictionary comprehension
sample dictionary {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
'''
def strDictConv(string):
    return {x: string.count(x) for x in string}


s = "hello"
print(s.count("he"))

'''
Given a list and dictionary, map each element of list with each item of dictionary
input: dic = {"four": 4, "nine": 9} list = [1, 2]
output: result = {1: {"four": 4}, 2: {"nine": 9}}
'''
dic = {"four": 4, "nine": 9}
list = [1, 2]

result = {}
index = 0
for key, value in dic.items():
    result[list[index]] = {key: value}
    index += 1


'''
Given an integer list, 
find the contiguous sublist (containing at least one number) which has the largest sum and return its sum.

input = [-2,1,-3,4,-1,2,1,-5,4]
sublist [4,-1,2,1] gives the largest sum 6, return 6

Input: nums = [5,4,-1,7,8]
output: 23
'''

dic = {num : num**2 for num in range(1, 11)}

d=dict()
for lol in range(1,11):
    d[lol]=lol**2
print(d)