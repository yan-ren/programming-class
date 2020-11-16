# # {} -> dictionary
# # [] -> list
# # () -> tuple, can be ignored
#
# example = {1: "one", "two": 2}
# print(example["two"])
# example[3] = "three"
# example[1] = "ONE"
# print(example)
#
# # exercise,
# # create a dictionary using loop, who has the pairs {0 : 1, 1 : 2, 2 : 3, ... 9 : 10}
# dic = {}
# for i in range(10):
#     dic[i] = i + 1
#
#
# # create a dictionary using loop,
# # where the sum of each key and value equals to 10
# # example:
# # d = {0: 10, 1:9, 2: 8, 3: 7, 4: 6, 5:5, 6:4, 7:3, 8:2, 9:1, 10:0}
# dic = {}
# for i in range(11):
#     dic[i] = 10 - i

sample = {1: "one", 2: "two", 3: 1}

if 3 in sample:
    sample[3] = sample[3] + 1
else:
    sample[3] = 1

# exercise
# given a dictionary {1: 1, 2: 1, 3: 1}
# check if a key from the input is in the dictionary,
# if in the dictionary, increase the value by one
# if not add the new key with value 1
# dic = {1:1, 2:1, 3:1}
# key = int(input("enter a number"))
# if key in dic:
#     dic[key] = dic[key] + 1
# else:
#     dic[key] = 1

# homework
# write a function that can build a histogram from a string
def histogram(word):
    pass

# input: "hello"
# output: {"h": 1, "e": 1, "l": 2, "o": 1}
# input: "yellow"
# output: {"y": 1, "e": 1, "l": 2, "o": 1, "w": 1}

# d = {"CS": [41, 106, 107], "LAW": [4093, 7007]}
# a = d.pop("CSC", "Nothing")
# print(d)
# print(a)

d = {1:1, 2:1, 3:1}
for key in d.keys():
    print(key)