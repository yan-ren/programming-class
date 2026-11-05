'''
basic data structure
- list
- tuple
- dictionary
- set

in dictionary values are in pair, key-value
'''
dict = {'red': 3, 'blue': 9} # key: 'red', value: 3
print(dict['red'])
dict.pop('red')
# print(dict['red'])

dict['yellow'] = 5

dict[25] = 5
dict[25] = 50
print(dict)

# dictionary with loop
# loop over the key
for k in dict:
    print(k, dict[k])

# loop over the values
for v in dict.values():
    print(v)

# loop by key and value
for k, v in dict.items():
    print(k, v)

# give you a string, find the most frequent letter
# 'abaacda' -> 'a'
s = 'abaacda'
count = {}

for ch in s:
    if ch in count:
        count[ch] += 1
    else:
        count[ch] = 1

print(count)

most_frequent = 0
most_frequent_letter = ''

for k, v in count.items():
    if v > most_frequent:
        most_frequent = v
        most_frequent_letter = k

print(most_frequent_letter)

d = {'class1': [10, 20, 30], 'class2': [60], 'class3': [7, 8, 9]}

from random import randint
d = dict.fromkeys(range(2, 12+1), 0)
print(d)

d = {'a': 1, 'b': 2, 'c': 3}
print(d.get('a'))
print(d['a'])

print(d['d']) # error
print(d.get('d', 0)) # try to get key 'd', if 'd' doesn't exist, give 0