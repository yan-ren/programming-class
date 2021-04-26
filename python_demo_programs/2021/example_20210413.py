'''
Write a python program to create a dictionary from a string
Given a string with all unique letters, the key of dictionary is the character in string,
where the value is the index of the character

s = "python"
d = {"p": 0, "y": 1, "t": 2, "h": 3, "o": 4, "n": 5}

s = "abc"
d = {"b": 1, "c": 2, "a": 0}
'''

# s = "abc"
# d = {i: s.index(i) for i in s}
#
#
# def sortStrDict(string):
#     returningDict = {}
#
#     for i in string:
#         # returningDict.update({i: string.index(i)})
#         returningDict[i] = string.index(i)
#
#     return returningDict
#
# # update the dictionary with the elements from another dictionary
# a = {"one": 1, "two": 2}
# b = {"three": 3}
# b.update(a)
# print(b)

s = "abc"
index = 0
dic = {}
for ch in s:
    dic[ch] = index
    index += 1