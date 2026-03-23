'''
for
+ range
+ string
+ list
+ dictionary
'''

s = 'abcd12345'

for ch in s:
    print(ch)

'''
indexing

'''
s = 'Arthur'
# print(s[0])
# print(s[2])
# print(len(s))
# print(s[5])
# print(s[-1])
# print(s[len(s) - 1])
# s_sub = s[0:2]
# print(s_sub)
for ch in s:
    print(ch)

i = 0
while i < len(s):
    print(s[i])
    i += 1
'''
palindrome
kayak
bob
'''
# solution1
# word = 'kayak'
# i = 0
# is_palindrome = True
# while i < len(word) / 2:
#     if word[i] != word[len(word) - i - 1]:
#         is_palindrome = False
#     i += 1
#
# if is_palindrome:
#     print('palindrome')
# else:
#     print('not palindrome')
#
# # solution2
# word = 'kayak'
#
# if word == word[::-1]:
#     print('palindrome')
# else:
#     print('not palindrome')

# # break
# i = 0
# while i < 3:
#     if i == 1:
#         break
#     print(i)
#     i += 1
#
# # continue
# i = 0
# while i < 3:
#     if i == 1:
#         i += 1
#         continue
#     print(i)
#     i += 1

# i = 0
# while i < 3:
#     j = 0
#     while j < 2:
#         print(j)
#         j += 1
#     i += 1

i = 0
while i < 4:
    j = 0
    while j < i + 1:
        print('*', end='')
        j += 1
    print()
    i += 1

'''
*
**
***
****
'''

'''
def

basic data structure
- list
- dictionary
- set
- tuple
'''

def welcome(name):
    print('Hello', name)
    print('Welcome to the class')

welcome('Tom')
welcome('Jerry')
welcome()