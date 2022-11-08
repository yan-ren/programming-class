'''
data structure

putting single value in one variable is not enough to handle complicate
we need better way to manage multiple values at the same time
that's why we need data structure

basic data structure
- list
- tuple
- dictionary
- set

'''
# l = [3, 4, 2, 1]
# l.sort()
# print(l)

'''
base on above how to do you find the largest value in the list?
'''

'''
tuple
you cannot make change to tuple once created -> immutable
()
[]
{}
'''
# t = (1, 2, 3, 4)
# print(t[0])
# # t[0] = 10
# t = (1, 2, 3)
# a, b = t
# print(a, b)

'''
recall the swap question:
exchange the value between to variables
a = 1
b = 2

how to let a and b swap their values
'''
# unpacking -> take the value from the tuple and assign to variable
# t = (1, 2)
# a, b = t

# a = 1
# b = 2
# a, b = (b, a)

'''
dictionary

what is a dictionary in real life
word -> meaning
word -> multiple meaning

word always on same page, word shows once in dictionary

in programming, for example python
key -> value
pair : key+value

key is unique, cannot have same key with different value
'''
d = {"one": 1, "two": 2, "three": 3}
# access
print(d["one"])
# print(d[1]) # invalid
d["one"] = 100
# print(d["four"])
d["four"] = 300
print(len(d))
del d["one"]
print(d)

# check if dictionary has key 'one'
# if "one" in d:
# get all keys from dictionary
d.keys()
# get all values()
d.values()
# get all pairs
d.items()

#  loop dictionary
for k, v in d.items():
    print(k, v)

'''
practice
how to create a dictionary as following
using loop
d = {1: 10, 2: 9, 3: 8, ... , 10:1}
'''
d = {}
for i in range(1, 11):
    d[i] = 11 - i

'''
given a string, find which letter has the highest frequency
s = "lecture'

s = 'abc'
for l in s:
    print(l)
    
d = {'a': 1}
if 'a' in d:
    d['a'] = d['a'] + 1

# loop dictionary
for k, v in d.items():
    print(k, v)
    
{'l':1, 'e':2...}


'''
d = {'a': 1, 'a': 2}
