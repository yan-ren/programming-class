
'''
python has type, but we don't need to write the type
python basic types:
- int
- float
- boolean
- string
'''
# a = int(input('enter a number:'))
# print('you just entered', a)
'''
dynamic typing
'''
# a = 1
# print(type(a))


# a = 1.0
# print(type(b))

# a = True
# a = False

# a = "abcde123"
# a = 'abcdedf'

# # 4 spaces or a tab
# if a > 2:
#     print('bigger')
#     print('smaller')
#     if a > 10:
#         print('bigger')

# elif a == 1:
#     print()

# i = 0
# while i < 10:
#     if i == 5:
#         break



# import time

# def max_sub_of_size_k_1(arr, k):
#     max_sum, window_sum, start_index = 0, 0, 0

#     for end in range(len(arr)):
#         window_sum += arr[end]

#         if end >= k-1:
#             max_sum = max(max_sum, window_sum)
#             window_sum -= arr[start_index]
#             start_index += 1
    
#     return max_sum


# # print(max_sub_of_size_k([2, 1, 5, 1, 3, 2], 3))

# def max_sub_of_size_k_2(nums, k):
#     count=0
#     biggest_sum=0
#     while count+k < len(nums):
#         if nums[count] + nums[count+1] + nums[count+2] > biggest_sum:
#             biggest_sum = nums[count] + nums[count+1] + nums[count+2]
#         count+=1
#     return biggest_sum

# # print(max_sub_of_size_k())

# test = [1] * 1000000000
# start_time = time.time()

# max_sub_of_size_k_2(test, 3)
# end_time = time.time()

# print(end_time - start_time)

# task1: loop through string and print each character
# 


'''
write a python code to check if a string is palindrome or not
palindrome is a word that reads the same from left to right and right to left
'''
# s = 'abcd'
# s[0]

# for i in range(0, 9, 2):
#     print(i)


import math


def isPalindrome(s):
  
  for i in range(int(len(s)/2)):
    if s[i] != s[len(s)-i-1]:
      return False

  return True

print(isPalindrome('kayak'))

'''
java: array, list, arraylist
java array: fix type, fix length
java list: fix type, length can grow
java arraylist is specific java list type

python: list
python list is used to store a list of value
'''
# l = []
# l.append(1)
# l.append(3.9)
# l.append('abc')
# print(l)

# l.remove(2)

# given a list of values, create a new list with all positive value
# l = [1, 2, -2, 3, 4, -2]
'''
create a new list
loop through the old list, check if value is positive, put the value into the new list
'''
# res = []
# for i in l:
#     if i > 0:
#         res.append(i)

# print(res)

def method1(a, b):

    return b, a


x, y = method1(1, 2)

'''
write a function: given two sorted int list, combine them to return a new sorted list
e.g
input:[1, 3, 5], [2, 4]
output:[1, 2, 3, 4, 5]
'''
def merge(l1, l2):
    res = []
    i = 0
    j = 0

    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            res.append(l1[i])
            i += 1
        else:
            res.append(l2[j])
            j += 1
    
    while i < len(l1):
        res.append(l1[i])
        i += 1
    
    while j < len(l2):
        res.append(l2[j])
        j += 1

    return res


# d = {}
# d[1] = 'a'
# d[2] = 'b'
# print(d)

'''
loop by keys
for k in d.keys():

loop by values
for v in d.value():

loop by key and value
for k, v in d.items():
'''

'''
give a string, find most frequent character inside
s = 'abcdefes'
'''

'''
list       -> java list
tuple      -> java array
dictionary -> java map
set        -> java set
'''
l = []
l.append(2)
l.append(1)
l.append(-2)
l.sort(reverse=True)
l.append([1, 2, 3])

# delete the value on index 0
del l[0]

# delete value 1
l.remove(1)

# delete the value on last index
l.pop()

# # check if one value is in the list
# if 2 in l:

# print(l)

# add all elements of a list to another list
a = [1, 2, 3]
b = [4, 5]
a.extend(b) # add all values in b into list a
print(a)
print(sum(a))
a[0] = 1
# given a list of values, remove all duplicates
# [1, 1, 2, 3, 2, 2]
# [1, 2, 3]
# a = (1, 2, 3, 4)
a = 1, 2, 3, 4, 5
print(type(a))
# a[0] = 100

'''
list: mutable
tuple: immutable
'''
def method():

    return 1, 2, 3

# unpacking
# tuple -> 3 integers
a, b, c = method()
print(type(a))

l = [1, 1, 2, 3]
sum(l)
min(l)
max(l)

'''
given a list of number, how to find the second largest value
'''

'''
dictionary: java map

values are in pair, key need immutable
'''
d = {}
d[1] = 'a'
d[2] = 'b'
d['key'] = 1

print(d)
print(d[1])

# update value
d[1] = 100

# remove key
d.pop(1) # if key doesn't exist, this raise an error

# # loop all keys
# for k in d.keys():

# # loop all values
# for v in d.values():

# # loop both key and value
# for k, v in d.items():

# if 1 in d:

'''
given a string, find most frequent character
e.g. 'abcddeaaa'
     'a'
'''
def most_frequent(s):
    dic = {}
    res = []
    for ch in s:
        if ch in dic:
            dic[ch] += 1
        else:
            dic[ch] = 1

    max_value = max(dic.values())
    for key, value in dic.items():
        if value == max_value:
            res.append(key)

    return res

# print(most_frequent('aabbc'))
def shortest_to_char(s, c):
    res = [0] * len(s)
    # loop from left to right
    # for each char, find the shortest distance to left side letter c
    index = 0
    c_position = len(s)
    while index < len(s):
        if s[index] == c:
            c_position = index
        res[index] = abs(index - c_position)
        index += 1
    # loo from right to left
    index = len(s) - 1
    while index >= 0:
        if s[index] == c:
            c_position = index
        res[index] = min(res[index], abs(index - c_position))
        index -= 1

    return res

print(shortest_to_char("loveleetcode", "e"))
