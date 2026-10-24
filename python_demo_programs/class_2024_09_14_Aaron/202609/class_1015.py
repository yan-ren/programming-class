'''
reverse a string: write a function that takes a string and returns revered string
e.g.
input: abc
return cba
'''
# def reverse_string(s):
#     result = ''
#
#     i = len(s) - 1
#     while i >= 0:
#         result += s[i]
#         i -= 1
#     return result
#
#
# print(reverse_string('abc'))

# def reverse_string(s):
#     if len(s) <= 1:
#         return s
#
#     return reverse_string(s[1:]) + s[0]
#
#
# print(reverse_string('abc'))

# def count(n):
#     print(n)
#
#     if n < 0:
#         return
#
#     count(n-1)

# 5! = 5 * 4 * 3 * 2 * 1

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

# check for a palindrome
# abccba -> True
# 'abc' -> False

def palindrome(s):
    if len(s) <= 1:
        return True

    if s[0] == s[-1]:
        return palindrome(s[1:len(s)-1])
    else:
        return False

