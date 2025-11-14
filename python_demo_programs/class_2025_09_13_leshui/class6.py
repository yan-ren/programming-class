'''
basic data structure in Python
- list
- dictionary
- tuple
- set

'''

# numbers = [1, 2, 1, 4, 2, 4]

# key:value -> pair
d = {'name': 'Alice', 'age': 12}
print(d['name'])
# print(d['Alice'])
d['name'] = 'Bob'

# if 'name' in d:
#
#
# del d['name']

# loop by key
for k in d:
    print(k)

# loop by value
for v in d.values():
    print(v)

# loop by key, value
for k, v in d.items():
    print(k, v)

'''
Given a string with letters, find the most frequent letter

e.g. 'aabcdeabd'
result = 'a'
'''
s = 'aabcdeabd'
d = {}

for ch in s:
    if ch in d:
        d[ch] += 1
    else:
        d[ch] = 1

print(d)

letter = ''
freq = 0

for k, v in d.items():
    if v > freq:
        freq = v
        letter = k

print(letter)