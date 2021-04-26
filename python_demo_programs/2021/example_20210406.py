# x = 2
# def foo(y):
#     z = 5
#     print(locals()['y']) # locals() returns a dict, key is the variable name, value is the variable value
#     print(globals()['x'])
#
# foo(3)

# x = 2
# if x > 0:
#     res = 'positive'
#
# print(res)
'''
Palindrome number
Given an integer x, return true if x is palindrome number
An integer is a palindrome whe it reads the same backward as forward
e.g. 121 is palindrome number while 123 is not
     12321
     
idea: convert given integer to string, then find if string is palindrome
'''
# def palindrome_number(x):
#     x = str(x)
#     return x == x[::-1]

x = 123
y = [True if str(x)[::-1] == str(x) else False][0]
# y is a list contains only one boolean
print(y)
