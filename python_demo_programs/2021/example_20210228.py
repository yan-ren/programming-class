# d = {'a': 20, 'b': 30, 'c': 10}
# # non comprehension
# new = {}
# for key, value in d.items():
#     if value <= 10:
#         new[key] = value
#
# print(new)
#
# new = {key:value for key, value in d.items() if value <= 10}
#
# dict = {'d':10, 'b':20}
# a = {key.upper():value for key,value in dict.items()}
# print(a)

# l = []
# l.append(1)
# print(l)
#
# for v in l:
#     print(v)
#
# i = 0
# while i < len(l):
#     print(l[i])
#
# l = (1, 2, 3)
# l = 1, 2, 3
# a, b = (1, 2, 3)

d = {'one': 1}
d['one'] = 1

'''
Write a Python script to concatenate following dictionaries to create a new one.

Sample Dictionary:
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50, 6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
'''