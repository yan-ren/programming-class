# exercise
# given a dictionary {1: 1, 2: 1, 3: 1}
# check if a key from the input is in the dictionary,
# if in the dictionary, increase the value by one
# if not add the new key with value 1

# d = {1: 1, 2: 1, 3: 1}
# key = int(input('enter the key'))
# if key in d:
#     d[key] = d[key] + 1
# else:
#     d[key] = 1

# write a function that takes a string as input, return the histogram
# 'aabcd'
# {'a': 2, 'b': 1, 'c': 1, 'd': 1}
def build_histogram(string):
    # hint: loop through the string by character, if the character in dictionary, increase the value by 1
    # else, add this character with value 1
    d = {}
    for c in string:
        if c in d:
            d[c] = d[c] + 1
        else:
            d[c] = 1
    return d

d = {1: 'one', 2: 'two', 3: 'three'}
# keys = list(d.keys())
# print(type(keys))
# print(keys)
#
# values = list(d.values())
# print(type(values))
# print(values)

# pairs = list(d.items())
# print(type(pairs))
# print(pairs)

# for key, value in d.items():
#     print(key, value)

# exercise
d = {1: 1, 2: 200, 3: 10}
# find the largest value together with its key in the dictionary
max = d.get(1)
max_key = 1
for key, value in d.items():
    if value > max:
        max = value
        max_key = key

# homework
# write a method takes a string as input,
# return the most used character in the string
# "aaaabc" -> "a"
# "abbbc" -> "b"
# "aabb" -> "a" or "b"
# hint:
# 1. create a dictionary from the string, where the key is the character
# value is the number of times this character is used in string
# 2. loop through the dictionary, find the key who has the largest value
def most_used_character(src):
    # build a histogram from a string, where the key is the character, value is how many times this character is used
    dic = {}
    for ch in src:
        if ch in dic:
            dic[ch] = dic[ch] + 1
        else:
            dic[ch] = 1
    # loop through the dictionary, find the key who has the largest value
    largest_key = ''
    largest_value = 0
    for key, value in dic.items():
        if value > largest_value:
            largest_value = value
            largest_key = key
    return largest_key
