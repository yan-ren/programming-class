'''
int
float
boolean
string
'''

# s = "123abc"

# indexing
# index = 0
# while index < len(s):
#     print(s[index])
#     index = index + 1

# index = len(s) - 1
# while index >= 0:
#     print(s[index])
#     index = index - 1

# s = 'abcdef'
# s_new = ''
#
# index = len(s) - 1
# while index >= 0:
#     s_new = s_new + s[index]
#     index = index - 1

s = 'abcdef'

# slicing
# s_new = s[0:3]
# print(s_new)
# print(s)

# s_new = s[1:4]
# print(s_new)

# s_new = s[:4] # s[0:4]
# s_new = s[1:]
# s_new = s[:]

# s_new = s[1:6:2] # start:end:step -> s[1]s[3]s[5]
# print(s_new)

# s_new = s[6:1:-2]
# print(s_new)

# s_new = s[::-1] # reversed string
# print(s_new)

l = [2, 1, 4, 5]
l.append(10)
print(l)

# calculate the sum of list

# index = 0
# s = 0
# while index < len(l):
#     s = s + l[index]
#     index = index + 1

# s = 0
# for value in l:
#     s = s + value
#
# print(s)

string = 'abc'
list = ['a', 'b', 'c']

# string[0] = 'w'
list[0] = 'w'
print(list)

for letter in string:
    print(letter)