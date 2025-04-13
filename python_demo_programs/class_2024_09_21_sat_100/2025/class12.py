'''
More about dictionary

dictionary is common in all programming languages, some languages call it Map
'''
import random

d = {}

d['one'] = 1
d[1] = 'one'
d['numbers'] = [1, 2, 3, 4, 5, 6]

print(d)

# given a string, how to count the number of each letters in it
s = 'abababc'
# {'a': 3, 'b': 3, 'c': 1}
d = {}
for letter in s:
    if letter in d:
        d[letter] += 1
    else:
        d[letter] = 1

print(d)

# complete problem: find the most frequent letter from a string
# 1. build the dictionary whose key is the letter, the value is the count
# 2. loop through the dictionary find the key whose value is the largest

# most_freq_letter = ''
# freq = -1
#
# for key, value in d.items():
#     if value > freq:
#         most_freq_letter = key
#         freq = value
#
# print(most_freq_letter)

# country_capitals = {
#     'France': 'Paris',
#     'Japan': 'Tokyo',
#     'India': 'New Delhi',
#     'Brazil': 'Brasilia'
# }
#
# print("🌍 Welcome to the Capital Guessing Game!")
# print('You will be given a country. Try to guess its capital.')
#
# countries = list(country_capitals.keys())
# score = 0
#
# for _ in range(3):
#     country = random.choice(countries)
#     capital = country_capitals[country]
#
#     guess = input(f'What is the capital of {country}?')
#
#     if guess == capital:
#         print("✅ Correct!")
#         score += 1
#     else:
#         print(f"❌ Wrong! The capital of {country} is {capital}.\n")
#
# print(f"🎉 Game over! You scored {score} out of 3.")

my_dict = {
    'brand': 'Toyota',
    'year': 2021
}

print(my_dict['year'])
# print(my_dict['name'])
print(my_dict.get('brand'))
print(my_dict.get('name', 'not exists'))

# removing item
del my_dict['brand'] # delete the key and value
my_dict.pop('year') # delete and return the value

# looping
for key, value in my_dict.items():
    print(key, value)

for key in my_dict.keys():
    print(key)

for value in my_dict.values():
    print(value)

'''
Create a dictionary of student names and their marks.

1. Print highest scorer
2. Calculate average marks

Invert a dictionary
original = {'a': 1, 'b': 2, 'c': 3}
output = {1: 'a', 2: 'b', 3: 'c'}
'''


