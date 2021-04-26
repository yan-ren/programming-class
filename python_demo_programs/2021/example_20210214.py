# list = [1, -2, -3, 4]
# a = ['positive'if i > 0 else 'negative' for i in list]
#
# a = []
# for i in list:
#     if i >= 0:
#         a.append('positive')
#     else:
#         a.append('negative')
#
# a = {'a':'b', 'b':'c'}
# b = {val:key for key, val in a.items()}
# print(b)

remove = {'apple', 'cherry'}
print(type(remove))
fruits = {'apple': 1, 'mango': 2, 'banana': 3, 'cherry': 4}
print(fruits.keys()) # returns all the keys in a set

# review: how to loop through a dictionary(3 ways)
dic = {1:"one", 2:"two"}
# loop by key
for k in dic.keys():
    print(k)
# loop by value
for v in dic.values():
    print(v)
# loop by pair
for k, v in dic.items():
    print(k, v)

# sort method, takes a list as input, returns a sorted list(smallest to largest), ascending order
l = [2, 4, 1, 0, 9]
print(sorted(l))
print(sorted(l, reverse=True))

# given a list of values, find the largest
# can you solve this question using sorted()
l = sorted(l)
print(l[len(l) - 1])

l = [10, 2, 4, 1]
l = sorted(l)
l.sort()
