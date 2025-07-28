'''
exercise 1: create a list with following numbers [1, 4, 9, 16, 25, 36, 49, 64, 81]
use loop and append
'''
# numbers = []
#
# for i in range(1, 10):
#     numbers.append(i * i)
#
# print(numbers)

'''
exercise 2: given a list of numbers e.g. [1, 2, -4, -2, 1]
create a new list from the given list only with positive values
e.g. [1, 2, 1]
'''
# numbers = [1, 2, -4, -2, 1]
# new_numbers = []
#
# for value in numbers:
#     if value > 0:
#         new_numbers.append(value)
#
# print(new_numbers)

# numbers = [[1, 2], [3, 4, 1]]
# sum = 0
# for sub in numbers:
#     for num in sub:
#        sum += num
# print(sum)

# given a list of numbers, calculate the sum of all numbers
# numbers = [1, 2, 1, 4, 5]
# sum = 0
#
# for num in numbers:
#     sum += num
#
# print(sum)

# list built-in function
# result = sum(numbers)
# print(result)
#
# s = 'abcde'
# print(s[3:5])
#
# numbers = [1, 2, 1, 3, 2]
# print(numbers[0:3])

'''
Given a list of numbers, and a target, find the index of the target in the list, 
if the target is not in the list, return -1

numbers = [1, 2, 4, 9, 5, 6]
target = 4
result = 2

target = 10
result = -1
'''
# numbers = [1, 2, 4, 9, 5, 6]
# target = 4
#
# result = -1
# index = 0
# while index < len(numbers):
#     if numbers[index] == target:
#         result = index
#     index += 1
#
# print(result)

'''
dictionary

cover slides: day13

real life dictionary:
word: meaning

python dictionary:
key: value

'''
# d = {}
#
# d['first_name'] = 'Smith'
# print(d)
#
# d['last_name'] = 'Bob'
# print(d)
# print(d['first_name'])
#
# d['first_name'] = 'Tom'
# print(d)

# if dictionary contains a key
# if 'first_name' in d:

# d = {'a': 1, 'b': 2, 'c': 2}
#
# for k in d:
#     print(k)
#
# for v in d.values():
#     print(v)
#
# for k, v in d.items():
#     print(k, v)

# given a string, count the frequency for each letter

# s = 'hello'
# d = {}
#
# for ch in s:
#     if ch not in d:
#         d[ch] = 1
#     else:
#         d[ch] += 1
#
# print(d)

# follow up: find which letter is the most frequent letter
# idea: loop through each key, value in dictionary, find which key has the largest value
# most_frequent = ''
# most_count = 0
# for k, v in d.items():
#     if v > most_count:
#         most_count = v
#         most_frequent = k
#
# print(most_frequent)

# Merge these two dictionaries into one:
# dict1 = {"a": 1, "b": 2}
# dict2 = {"a": 3, "d": 4}
#
# dict3 = {}
#
# for k, v in dict1.items():
#     dict3[k] = v
#
# for k, v in dict2.items():
#     if k in dict3:
#         dict3[k] = dict3[k] + v
#     else:
#         dict3[k] = v
#
# print(dict3)

scores = {"Alice": 88, "Bob": 95, "Charlie": 90}

# calculate the avg score
total = 0
for v in scores.values():
    total += v

print(total / len(scores))

# find the person with the highest score
highest_score = 0
person = ''

for k, v in scores.items():
    if v > highest_score:
        highest_score = v
        person = k

print(person)


'''
exercise:
# Given: marks = {"Alice": 90, "Bob": 65, "Eve": 82}
# Create a new dictionary with only students who scored above 80.

redo the count character in a string
'''