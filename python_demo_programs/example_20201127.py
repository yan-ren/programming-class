# practice
# Below are the two lists convert it into the dictionary
# keys = ['Ten', 'Twenty', 'Thirty', 'Hello']
# values = [10, 20, 30, 'Hi']
# expected output: {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Hello': 'Hi'}

# create a dictionary from two lists, one list has all keys, one list has all values
def build_dictionary(keys, values):
    dic = {}
    for i in range(len(keys)):
        dic[keys[i]] = values[i]

    return dic

# homework
# merge following two dictionaries into one
# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# expected output
# hidden condition: for the same keys in both dictionary, they have the same value
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

def merge(dic1, dic2):
    # loop through dic1, put each key value into dic2, and return dic2
    for key, value in dic1.items():
        if key not in dic2:
            dic2[key] = value
        else:
            dic2[key] = dic1[key] + dic2[key]
    return dic2

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
print(merge(dict1, dict2))

# merge following two dictionaries into one
# for the same key in both dictionary, combine the value
# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 300, 'Fourty': 40, 'Fifty': 50}
# expected output
# {'Ten': 10, 'Twenty': 20, 'Thirty': 330, 'Fourty': 40, 'Fifty': 50}

# dic = {}
# s = set()
# student = {'Atonio', 'Tim'}
# print(type(student))

# l = [1, 1, 1, 1]
# s = set(l)
# print(s)
#
# s.add(2)
# print(s)
#
# s.add(1)
# print(s)
#
# s.remove(1)
# print(s)
# s.remove(1)
# print(s)

# basket = {'orange', 'banana', 'pear', 'apple'}
# print(basket)
# for fruit in basket:
#     print(fruit, end=':)')
empty_set = set()
empty_set.add(1)
print(empty_set)
empty_set.update({2, 3, 4})
print(empty_set)

# exercise
# how to determine if a string has no duplicate characters
# s = "abc"
# s = "aab"
# s = "abc"
# if len(s) == len(set(s)):
#     print('none duplicate characters')

# a = {1, 2, 3}
# b = {2, 4}
# print(a - b)
# print(b - a)

# homework
# given a dictionary, create a set with all keys and values from the dictionary
# dic = {"one": 1, "two": 2}
# {"one", "two", 1, 2}