'''
Two keywords used inside loop
- break
- continue
'''

# index = 0
# while index < 4:
#     if index == 2:
#         index += 1
#         continue
#
#     print(index)
#     index += 1

'''
while + string
'''
s = 'arthur'
# print(s[0])
# print(s[1])
# print(s[2])
# print(s[3])
# print(s[4])
# print(s[5])

# i = 0
# while i < len(s):
#     print(s[i])
#     i += 1
#
# # how to print each letter in reverse order
# i = len(s) - 1
# while i >= 0:
#     print(s[i])
#     i -= 1

# s = 'abcdef'
#
# if 'a' in s:

# if given a string, count how many vowels inside
s = 'hello welcome'

index = 0
counter = 0

while index < len(s):
    # if s[index] in 'aeiou':
    if s[index] == 'a' or s[index] == 'e' or s[index] == 'i' or s[index] == 'o' or s[index] == 'u':
        counter += 1

    index += 1

print(counter)

# given a string, create a new string in reversed order
# e.g. 'abc' -> 'cba'

# s = 'abc'
# s_rev = ''
#
# index = 0
# while index < len(s):
#     s_rev = s[index] + s_rev
#     index += 1
#
# print(s_rev)

'''
given a string, create a new string without vowels
e.g.
s = 'hello'
s_new = 'hll'
'''