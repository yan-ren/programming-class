a = 1
b = 1.0
c = a

# double equal compares the value
print(a == b)
# is operator compares if the two object is the same
print(a is b)
print(a is c)
'''
Write a Python script to concatenate following dictionaries to create a new one.

Sample Dictionary:
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50, 6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

basic idea, loop through each dictionaries and put each key value into the new dictionary,
you can put three dictionaries into a list, then loop through the list
'''
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50, 6:60}

new_dic = {}
for d in [dic1, dic2, dic3]:
    # loop through key, value of d
    for key, value in d.items():
        new_dic[key] = value

'''
Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) 
and the values are square of keys
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
'''
lol = dict()
for x in range(1, 16):
    lol[x] = x**2
print(lol)

'''
write a python function called multiply_values, the function multiplies all the values in a dictionary
'''
lol = {1:3, 5:6, 7:9}
def multiply_values(x):
    res = 1
    for value in x.values():
        res = res * value
    return res

print(multiply_values(lol))

'''
Write a Python function to combine two dictionaries adding values for common keys.
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})

d1 = {'a': 100}
d2 = {'a': 200}
{'a': 100, 'b': 200}
'''
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}

# how to put all keys/values in d1 into d2
# loop through key/value in d1 and put it into d2
for key, value in d1.items():
    if key in d2:
        d2[key] = d1[key]+d2[key]
    else:
        d2[key] = value

# def combine(d1, d2):
#     for key, value in d1.items():
#         if key in d2:
#             d2[key] = d2[key] + value
#         else:
#             d2[key] = value
#     return d2
#
#
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# print(combine(d1, d2))

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d3 = {}
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})

a = 1
if a > 0:
    b = "positive"

print(b)

'''
Convert two lists into the dictionary
example:
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

output:
{'Ten': 10, 'Twenty': 20, 'Thirty': 30}
'''
