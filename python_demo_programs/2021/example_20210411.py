'''
given two lists a=["one", "two", "three"] b=[1,2,3]
covert two lists into a dictionary d = {"one":1, "two":2, "three":3}
'''

# luke
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# dic = {}
# counter = 0
#
# for i in keys:
#     dic[i] = values[counter]
#     counter += 1
#
# print(dic)
#
#
# index = 0
# while index < len(keys):
#     dic[keys[index]] = values[index]
#     index += 1
#
#
# # Jesse
# keys = ['ten', 'twenty', 'thirty']
# values = [10, 20, 30]
# plop = {}
# for d in keys:
#     for c in values:
#         plop[d] = c
#         values.remove(c)
#         break
#
# print(plop)
#
# for i in range(10):
#     if i % 2 == 1:
#         continue
#     print(i)

'''
Write a python program to create a dictionary from a string
Given a string with all unique letters, the key of dictionary is the character in string, 
where the value is the index of the character

s = "python"
d = {"p": 0, "y": 1, "t": 2, "h": 3, "o": 4, "n": 5}

s = "abc"
d = {"b": 1, "c": 2, "a": 0}
'''
# x = 2
# def foo(y):
#     z = 5
#     print(locals()['y'])
#     print(globals())
#     print(x, y, z) # what's the rule that computer searches for variable
#
#
# foo(3)

# x = 1
# if x > 0:
#     y = "positive"
#
# print(y)

d = {"one": 1, "two": 2, "three": 3}
# print(d["one"]) # one way to get the value by key, but will fail if don't have the key
# print(d.get("four")) # another way, get None if don't have the key

string = 'hello world'
counter = 0
output = {}
for i in string:
    output[i] = counter
    counter += 1
print(output)

