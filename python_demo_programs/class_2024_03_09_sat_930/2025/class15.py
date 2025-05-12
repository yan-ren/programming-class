# dictionary comprehension
# how to create a dictionary with following values
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# d = {}
# for i in range(1, 6):
#     d[i] = i**2
#
# print(d)
#
# d = {i:i**2 for i in range(1, 6)}
# print(d)

original_dict = {'a': 1, 'b': 2, 'c': 3}
# Output: {1: 'a', 2: 'b', 3: 'c'}
# new_dict = {}
# for key, value in original_dict.items():
#     new_dict[value] = key
#
# print(new_dict)
#
# new_dict = {value: key for key, value in original_dict.items()}

# Output: {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}
# original_dict = {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}
# even_dict = {}
#
# for i in range(10):
#     if i % 2 == 0:
#         even_dict[i] = i ** 2
#
# print(even_dict)
#
# even_dict = {i: i**2 for i in range(10) if i % 2 == 0}

matrix = [[(row, col) for col in range(3)] for row in range(3)]

# without comprehension
matrxi = []
for row in range(3):
    for col in range(3):
        matrxi.append((row, col))


'''exercise 1
words = ['hello', 'world', 'python', 'programming']
Output: {'hello': 5, 'world': 5, 'python': 6, 'programming': 11}
'''

'''exercise 2
# Output: {1: 'odd', 2: 'even', 3: 'odd', 4: 'even', 5: 'odd'}
'''