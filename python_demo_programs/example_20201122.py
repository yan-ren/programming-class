# exercise
# write a method takes two dictionaries as input, dic1 and dic2
# return a dictionary contains the common key - value pair in dic1 and dic2
# example
# dic1 = {1: 1, 2: 2, 4: 4}
# dic2 = {1: 100, 3: 3, 4: 4}
# {1: 101, 4: 8}
def common(dic1, dic2):
    # loop through dic1, for each key check if in the dic2
    # if in the dic2, add key with value dic1[key] + dic2[key] into new dictionary
    dic = {}
    for key, value in dic1:
        # check if key is also in dic2
        if key in dic2:
           dic[key] = dic1[key] + dic2[key]

    return dic

# loop a dictionary
dic = {1: 1, 2: 2, 3: 3}
# keys = dic.keys()
# print(type(keys))
# print(keys)
#
# for key in keys:
#     print(dic[key])
#
# values = dic.values()
# print(type(values))
# print(values)
#
# for v in values:
#     print(v)
# pairs = dic.items()
# print(type(pairs))
# print(pairs)
# for key, value in pairs:
#     print(key, value)

# write a method takes two dictionaries, dic1 and dic2, remove the key from dic1, if the same key is also in the dic2
# dic1 = {1: 1, 2: 2, 4: 4}
# dic2 = {1: 100, 3: 3, 4: 4}
# {2: 2}
# solution1: loop through dic1, if key is not in dic2, put this key in new dictionary
def remove_common(dic1, dic2):
    dic = {}
    for key, value in dic1:
        if key not in dic2:
           dic[key] = dic1[key]

    return dic

# def remove_common(dic1, dic2):
#     # get all keys in dic1 put them in a list, then loop this list
#     keys = list(dic1.keys())
#     for key in keys:
#         if key in dic2:
#             del dic1[key]
#     return dic1

# remove_common({1: 1, 2: 2, 4: 4}, {1: 100, 3: 3, 4: 4})

# homework
# given two dictionaries with no common keys, combine them into one dictionary
# input: dic1 = {1: 1, 2: 2}, dic2 = {3: 3}
# return {1: 1, 2: 2, 3: 3}
# def combine_dic(dic1, dic2):
#     # hint: loop through one dictionary and put each key-value pairs into another dictionary
#     for