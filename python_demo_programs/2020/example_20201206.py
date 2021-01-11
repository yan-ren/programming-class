# # key points of list
# l = []
# l.append(1)
# # remove by value
# l.remove(1)
# # delete by index
# del l[0]
# len(l)
# # check contains
# # if 1 in l:
# # loop through the list
# index = 0
# while index < 0:
#     print(l[index])
#     index += 1
#
# for i in l:
#     print(i)

# exercise
# write a function that takes a number list as input,
# return the sum of all positive number and all negative numbers
# input = [1, -1, 2, -3]
# expected 3, -4

# loop dictionary
# by keys
dic = {"one": 1, "two": 2, "three": 3}
for key in dic.keys():
    print(key)

for value in dic.values():
    print(value)

for a, b in dic.items():
    print(a, b)

# exercise
# given a dictionary whose values are all numbers, find the key whose value is the largest
# dic = {"one": 1, "two": 2, "three": 3}
# "three"

dic = {"one": 1, "two": 2, "three": 3}
largest_key = 0
largest_value = 0
for key, value in dic.items():
    if value > largest_value:
        largest_value = value
        largest_key = key

print(key)

# homework1: given a dictionary, extract all the keys into a list
# given: dic = {"one": 1, "two": 2, "three": 3}
# expected: ["one", "two", "three"]

# homework2: Delete set of keys from Python Dictionary
# given: dic = {"three": 3},
# ["one", "two", "four"]
# expected output: dic = {"three": 3}

def remove_keys(dic, keys):
    for key in keys:
        if key in dic:
            del dic[key]
    return dic

remove_keys({"one": 1, "two": 2, "three": 3}, ["one", "two"])

# exercise, given a dictionary, extract all the keys and values into a list
# given: dic = {"one": 1, "two": 2, "three": 3}
# expected: ["one", 1, "two", 2, "three", 3]
dic = {"one": 1, "two": 2, "three": 3}
l = []
for key, value in dic.items():
    l.append(key)
    l.append(value)