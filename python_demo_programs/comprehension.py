'''
list comprehension
dicitonary comprehension
set comprehension
'''

'''
list comprehension

create a new list base on exisiting list/loops
'''
# numbers = [1, 2, 3, 4, 5]

# squares = []
# for num in numbers:
#     squares.append(num*num)

'''
[expression for item in list]
'''
# l = [num*num for num in numbers]

# numbers = [-1, 2, 2, -1]

# positive = []
# for num in numbers:
#     if num > 0:
#         positive.append(num)
#     else:
#         positive.append(-num)

# [num if num > 0 else -num for num in numbers]


'''
exercise: given a list of numbers [1, 2, 3, 4]
for each number, if even, put 'even' into the list
if odd, put 'odd' into the list

['odd','even', 'odd', 'even']
generate new list using comprehension
'''

# ['even' if num % 2 == 0 else 'odd' for num in numbers]

# dic = {'a':1, 'b':2, 'c':3}
# # create a new dictionary using loops
# {val:key for key, val in dic.items()}

'''
given a list ['apple', 'banana']
create a dicionary, key is the string and value is the length of string
'''
# list = ['apple', 'banana']
# {s:len(s) for s in list}


# numbers = [1, 2, 3, 4]
# squares = []

# for n in numbers:
#     squares.append(n*n)


# comprehension: list, dictionary, set
# l = [n*n for n in numbers]

# [expression for loop]

# numbers = [1, -2, 3, -4, 5]
# create a new list with all numbers times negative one [-1, -2, -3, -4, -5]
# create a new list with absolute value, [1, 2, 3, 4, 5]

# abs = []
# for n in numbers:
#     if n > 0:
#         abs.append(n)
#     else:
#         abs.append(-n)

# [n if n > 0 else -n for n in numbers]

# sentence = 'IHaveADream'
# result = [word.lower() for word in sentence]
# print(result)

# # create a new list with all non-vowel letter
# # ['h', 'v', 'd', 'r', 'm']

# [c for c in sentence.lower() if c not in 'aeiou']

# seq = [1, 2, 3]
# [(x, x**2, x**3) for x in seq]

'''
java: array, list(arraylist, linkedlist)
python: tuple, list
'''

# t = (1, 2, 3)
# print(t[0])
# t[0] = 100

'''
[0, 1, 2, 3] -> [1, 3, 5, 7]
[3, 8, 9, 5] -> [True, False, True, False]

['apple', 'orange', 'pear'] -> ['A', 'O', 'P']
['apple', 'orange', 'pear'] -> [('apple', 5), ('orange', 6), ('pear', 4)]
 
 
 

'''
# arr = [3, 8, 9, 5]
# [n%3==0 for n in arr]

# '''
# dictionary comprehension
# {expression for loop}
# '''
# # animals = {'micheal':'elephant', 'sam': 'ox'}

# # {value:key for key, value in animals.items()}

# fruit = ['apple', 'orange', 'pear']
# {"apple": 5, "orange": 6, "pear": 4}

n = 1_000_000
print(n)

a = "hello"
b = "world"
print(a + b)
print(a * 5)

print(4 / 2)
print(4 // 2)