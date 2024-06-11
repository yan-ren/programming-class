# d = {'names': ['Tom', 'Jerry']}
#
# print(d['names'])

# d = {'address': {'street': '123 main street', 'city': 'New York'}}
# print(type(d['address']))
# print(d['address']['street'])

# d = {'a': 1, 'b': 2, 'c': 3}

'''
loop each key value pairs in dictionary
'''
# loop by key
# for k in d.keys():
#     print(k)
#     print(d[k])
#
# for k, v in d.items():
#     print(k, v)
#
# list = [1, 2, 3]
#
# def method1(l):
#     l.append(4)
#
# def method2(l):
#     l = [1]
#
#
# method2(list)
# print(list)

# d1 = {'a': 1, 'b': 2}
# d2 = {'c': 1, 'd': 2}
#
# def merge_dic(d1, d2):
#     new_d = {}
#     for k, v in d1.items():
#         new_d[k] = v
#     for k, v in d2.items():
#         new_d[k] = v

s = set()
s.add(1)
s.add(2)
print(s)

s.add(1)
print(s)

'''
recall: remove duplicate value from list
e.g. list = [1, 2, 1, 1, 4]
-> [1, 2, 4]
'''
# numbers = [1, 2, 1, 1, 4]
# numbers = list(set(numbers))
# # discrate math
# print(numbers)

# s1 = {1, 2, 3}
# s2 = {3, 4, 5}
#
# union_set = s1.union(s2)
# print(union_set)
#
# intersetion_set = s1.intersection(s2)
# print(intersetion_set)
#
# difference_set = s1.difference(s2)
# print(difference_set)
#
# difference_set = s2.difference(s1)
# print(difference_set)

def super_union(s1, s2, s3):
    set_list = []
    set_list.append(s1)
    set_list.append(s2)
    set_list.append(s3)

    res = set()
    for s in set_list:
        res = res.union(s)

    return res


s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = {3, 4, 5}

res = super_union(s1, s2, s3)

'''
Valid Anagram
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

e.g. abc <-> cba


Find most frequent letter in string
Given a string s, return the most frequent letter in s

Merge two dictionaries
Write a function that merges two dictionaries. If a key is present in both dictionaries, sum the value

e.g. 
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}

dict3 = {'a': 1, 'b': 5, 'c': 7, 'd': 5}
'''
def build_dic(str):
    char_dic = {}
    for char in str:
        if char in char_dic:
            char_dic[char] += 1
        else:
            char_dic[char] = 1

    return char_dic

def anagram(str1, str2):
    char_dic1 = build_dic(str1)
    char_dic2 = build_dic(str2)

    # if char_dic1 == char_dic2:
    #     return True
    # else:
    #     return False
    return char_dic1 == char_dic2