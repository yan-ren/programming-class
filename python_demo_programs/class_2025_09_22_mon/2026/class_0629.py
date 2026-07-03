'''
ryanren3343
'''

'''
data structure in python
- list
- tuple
- dictionary
- set
'''
# people = {'name': 'bob', 'age': 20}
# print(people['name'])
# print(people['age'])
# people['age'] = 21
#
#
# people['address'] = 'montreal'
# print(people)
#
# # dictionary does allow duplicated key
# if 'name' in people:
#     print(people['name'])
#
#
# # loop by key
# for k in people.keys():
#     print(k, people[k])
#
# # loop by value
# for v in people.values():
#     print(v)
#
# # loop by k, v
# for k, v in people.items():
#     print(k, v)

'''
given a string with letters, use dictionary as counter to conut how many times that each letter shows up

e.g.
text = 'abcaabcd'

'''
text = 'abcaabcd'
count = {}

for ch in text:
    if ch in count:
        count[ch] += 1
    else:
        count[ch] = 1

print(count)

freq = 0
freq_letter = ''

for letter, c in count:
    if c > freq:
        freq = c
        freq_letter = letter

print(freq_letter)