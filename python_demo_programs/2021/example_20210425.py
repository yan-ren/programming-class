'''
global scope: the scope outside of function
local scope: the scope inside the function

global variable: the variable on the global scope
local variable: the variable on the local scope

default behaviour 1: if variable is defined inside function,
by default it's defined on local scope
default behaviour 2: when program uses a variable inside function, program first
searches the variable on the local scope, if variable not found,
continue search on the global scope
rule: inside a function, a variable cannot be both on local scope and global scope
'''

# def foo():
#     global s # force to use global s, change default behaviour
#     print(s) # print global s
#     s = "That's clear." # set global s = “That’s clear”
#     print(s)  # print global s
#
#
# s = "Python is great!"
# foo()
# print(s) # ?

def calculation():
    global place
    place = "Cape Town"
    global name # define a global variable inside a function
    name = "John"


place = "Berlin"
calculation()
print(place)
print(name)