'''
dictionary: word -> meaning
word only showed in one place

dictionary: key -> value
key cannot be duplicated
'''
d = {'name': 'Tom', 'age': 20}
print(d['name'])
d['name'] = 'Jerry'
d['grade'] = 12

del d['grade']

for k in d.keys():
    print(k)

for k, v in d.items():
    print(k, v)

for v in d.values():
    print(v)

grades = {'Tom': 90, 'Jerry': 29, 'Bob': 89, 'Kim': 30}

# find who is lower than 60
# names = []
# for name, score in grades.items():
#     if score > 60:
#         names.append(name)
#
# print(names)

'''
given a dictionary
grades = {'Tom': 90, 'Jerry': 29, 'Bob': 89, 'Kim': 30}

keep all grades that is bigger than 60
grades = {'Tom': 90, 'Bob': 89}

'''