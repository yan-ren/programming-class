'''
python collection
- list
- tuple
- map
- set
'''

numbers = [1, 2, 4, 1]
numbers.sort(reverse=True)
print(numbers)

s = '1,2,3,4'
print(s.split(','))

names = ['abc', 'bcd', 'aec']
print(':'.join(names))

s = 'abcd'
print(list(s))

'''
You are given:

A list of integers numbers.
A string s containing numbers separated by commas.

Your task is to:

Sort numbers in descending order.
Extract even numbers from the sorted list and store them in a new list.


Example:
numbers = [3, 1, 4, 2]
res = [4, 2]

s = '10,20,30'
l = [11, 21, 31] 
'''
l = [11, 21, 31]

for i in range(len(l)):
    l[i] = int(l[i])


d = {}
d['a'] = 1
d['ab'] = 10
print(d)
for k in d.keys():
    print(k, d[k])

'''
nums = [3, 1, 2, 2, 3, 3, 4]
{1: 1, 2: 2, 3: 3, 4: 1}
'''

'''
dict1 = {"a": 2, "b": 3, "c": 1}  
dict2 = {"b": 4, "c": 2, "d": 5}

{"a": 2, "b": 7, "c": 3, "d": 5}

'''

'''
data = {"apple": 5, "banana": 3, "cherry": 5, "date": 2}

{5: ["apple", "cherry"], 3: ["banana"], 2: ["date"]}

'''
data = {"apple": 5, "banana": 3, "cherry": 5, "date": 2}
new_data = {}
for key, value in data.items():
    if value in new_data:
        new_data[value].append(key)
    else:
        new_data[value] = [key]

print(new_data)