'''
review dictionary
'''
# d = {'name': 'Bob', 'age': 9}
# print(d['name'])
# print(d['age'])
# d['age'] = 10
# print(d)
# d['address'] = 'montreal'
# del d['age']
#
# for k in d.keys():
#     print(k, d[k])
#
# for v in d.values():
#     print(v)
#
# for k, v in d.items():
#     print(k, v)

grades = {'math': [90, 89, 67, 39], 'english': [29, 32, 41, 45], 'french': [80, 67, 34, 59]}
# find highest and lowest grade in each subject
for sub, marks in grades.items():
    highest = marks[0]
    lowest = marks[0]
    for m in marks:
        if m > highest:
            highest = m
        elif m < lowest:
            lowest = m
    print(sub + " highest " + str(highest) + " lowest " + str(lowest))