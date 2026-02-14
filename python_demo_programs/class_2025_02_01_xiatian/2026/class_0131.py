'''
dictionary
'''
d = {'name': 'Tom', 'age': 21}
# print(d['name'])
# print(d['age'])
# d['grade'] = '12'
# print(d)
#
# del d['grade']

for k, v in d.items():
    print(k, v)

for k in d:
    print(k)

for v in d.values():
    print(v)

grade = {'Tom': 90, 'Jerry': 89, 'Peter': 60, 'Tim': 59}

# find the average

# find how many people failed, and their name

s = 'helloworld'
freq = {}

for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print(freq)

freq_letter = ''
most_freq = 0

for k, v in freq:
    if v > most_freq:
        most_freq = v
        freq_letter = k

'''
given a dictionary, e.g. {'Tom': 90, 'Bill': 87, 'Tim': 56}
remove failed people
e.g.
{'Tom': 90, 'Bill': 87}

'''
d = {'Tom': 90, 'Bill': 87, 'Tim': 56}
new_d = {}

for k, v in d.items():
    if v > 60:
        new_d[k] = v

print(new_d)

