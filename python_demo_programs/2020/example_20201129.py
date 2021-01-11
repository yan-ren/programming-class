# homework
# given two dictionaries with no common keys, combine them into one dictionary
# input: dic1 = {1: 1, 2: 2}, dic2 = {3: 3}
# return {1: 1, 2: 2, 3: 3}
dic = {"one":1, "two": 2, "three": 3}
# loop through keys
for key in dic.keys():
    print(key)
# loop through values
for value in dic.values():
    print(value)
# loop through items/pairs
for key, value in dic.items():
    print(key, value)


def combine_dic(dic1, dic2):
#     # hint: loop through one dictionary and put each key-value pairs into another dictionary
    for key, value in dic1.items():
        dic2[key] = value

    return dic2


# given two dictionaries, combine them into one dictionary
# for the same key in both dictionary, add the key and sum of the values
# input: dic1 = {1: 1, 2: 2}, dic2 = {2: 4, 3: 3}
# return {1: 1, 2: 4, 3: 3}
def combine_dic2(dic1, dic2):
    for key, value in dic1.items():
        if key in dic2:
            dic2[key] = dic1[key] + dic2[key]
        else:
            dic2[key] = value

    return dic2

dic1 = {1: 1, 2: 2}
dic2 = {2: 4, 3: 3}
print(combine_dic2(dic1, dic2))

# given two lists combine them into a dictionary
# ["one", "two", "three"]
# [1, 2, 3]
# expected output: ["one": 1, "two": 2, "three": 3]
# notice these two lists have to be in the same length,
# loop through lists by index, put values from each list as key value pairs
l1 = [1, 2, 3]
l2 = [4, 5, 6]
dic = {}
index = 0
while index < len(l1):
    dic[l1[index]] = l2[index]