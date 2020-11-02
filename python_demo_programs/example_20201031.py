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

# homeword: write a function merge two Python dictionaries into one
'''
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

{'Ten': 10, 'Twenty': 20, 'Thirty': 60, 'Fourty': 40, 'Fifty': 50}
'''