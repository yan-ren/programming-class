def return_multiple():
    a = 1
    b = 2
    return a, b

c = return_multiple()
print(c)
print(type(c))

# Given a tuple of lists, write a Python program to unpack the elements of the lists that are packed inside the given tuple.
'''
Examples:

Input : (('a', 'apple'), ('b', 'ball'))
Output : ['a', 'apple', 'b', 'ball']

Input : ([1, 'sam', 75], [2, 'bob', 39], [3, 'Kate', 87])
Output : [1, 'sam', 75, 2, 'bob', 39, 3, 'Kate', 87]
'''
# def unpack_tuple(src):


def quick_math(a, b, c):
    return a + b - c

boom = (1, 2, 3)
quick_math(*boom)

# homework: write a function merge two Python dictionaries into one
'''
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

{'Ten': 10, 'Twenty': 20, 'Thirty': 60, 'Fourty': 40, 'Fifty': 50}
'''
def merge_dictionaries(dict1, dict2):
    for i in dict2:
        # check key i in dict1, if not, put key:i and value:dict2[i] in dict1
        if i not in dict1:
            dict1[i] = dict2[i]
        # if in dict1, update key: i with dict1[i] + dict2[i]
        else:
            dict1[i] = dict1[i] + dict2[i]

# write a function takes two dictionaries, return the dictionary only has the common key and value combined
# d1 = {1:1, 2:2}
# d2 = {2:2, 3:3}

# return {2:4}

# Write a Python program to check
# if a set is a subset of another set

# write a function takes a dictionary and return a set contains all keys and values
# input {1: "one", 2: "two", 3: "two"}
# output {1, "one", 2, "two", 3}
