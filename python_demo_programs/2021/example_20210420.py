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