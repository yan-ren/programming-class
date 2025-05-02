# numbers = [1, 2, 1, 4]
#
# for num in numbers:
#     print(num)
from class_2025_02_22_sat_300.class4 import correct_number

# d = {"one": 1}
# print(d['one'])
# d['two'] = 2
#
# print(d)
#
# del d['one']
#
# print(d)

student = {
    "name": "Alice",
    "age": 20,
    "grade": "A"
}

car = {}
car['brand'] = "Toyota"
car['model'] = "Corolla"
car['year'] = 2020
print(car)

person = {
    "name": "John",
    "age": 30,
    "is_student": False,
    "hobbies": ["reading", "cycling", "gaming"]
}
print(person)

# if 'name' in person:

fruits = {"apple": 2, "banana": 5, "cherry": 10}

for fruit, quantity in fruits.items():
    print(fruit, quantity)

price = 0
for fruit in fruits.keys():
    print(fruit, fruits[fruit])
    price += fruits[fruit]

'''
1. Count Word Occurrences
Write a program that asks the user for a sentence and counts how many times each word appears.

Input: "cat dog cat"
Output: {'cat': 2, 'dog': 1}
'''
sentence = input('Enter a sentence:')
words = sentence.split()
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)

# follow up: find the most frequent word
most_frequent_word = None
max_count = 0

for word, count in word_count.items():
    if count > max_count:
        max_count = count
        most_frequent_word = word

print("Word counts:", word_count)
print("Most frequent word:", most_frequent_word)
print("Frequency:", max_count)

# review: given a list of value, find the largest number
numbers = [2, 1, 5, 20, 6]

'''
Given a dictionary where keys are names and values are favorite colors:

favorite_colors = {"Alice": "blue", "Bob": "green", "Charlie": "blue"}

Create a new dictionary where the keys are colors and the values are lists of names who like that color.

{'blue': ['Alice', 'Charlie'], 'green': ['Bob']}

'''
favorite_colors = {"Alice": "blue", "Bob": "green", "Charlie": "blue"}

color_to_name = {}

for name, color in favorite_colors.items():
    if color in color_to_name:
        color_to_name[color].append(name)
    else:
        color_to_name[color] = [name]

print(color_to_name)

'''
Task:
Given two dictionaries:

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
Write code to merge them into one.
If a key exists in both, add their values together.

Result:
{'a': 1, 'b': 5, 'c': 4}
'''

