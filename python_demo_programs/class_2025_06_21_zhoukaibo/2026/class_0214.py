'''
list
tuple
dictionary
set
'''

t = (2, 3, 4)
print(t)
t[0] = 20
print(t)

# d = {'age': 21, 'name': 'Tom'}
# print(d['age'])
# d['age'] = 22
#
# for k in d.keys():
#     print(k, d[k])
#
# for k, v in d.items():
#     print(k, v)
#
# for value in d.values():
#     print(value)

# d = {('age', 'name'): [21, 'Tom']}

text = 'hellowelcome'

count = {}
for ch in text:
    if ch not in count:
        count[ch] = 1
    else:
        count[ch] += 1

max_value = 0
for value in count.values():
    if value > max_value:
        max_value = value

for key, value in count.items():
    if value == max_value:
        print(key)