'''
Ask user to type three integers, print the largest integer
assume all numbers are different
'''
# first = int(input('Enter the first value:')) # '12' -> 12
# second = int(input('Enter the second value:'))
# third = int(input('Enter the third value:'))

# solution 1
# if first > second and first > third:
#     print('First number is the largest')
# elif second > first and second > third:
#     print('Second number is the largest')
# else:
#     print('Third number is the largest')

# solution 2
# nested if statement
# if first > second:
#     if first > third:
#         print('First number is the largest')
#     else:
#         print('Third number is the largest')
# else:
#     if second > third:
#         print('Second number is the largest')
#     else:
#         print('Third number is the largest')

'''
String type

Python string: a string is quoted by single or double quoted with zero or more characters

character: letters numbers symbols
abcd, 12345, !@#$%^
'''
# s_a = 'abc123!@#$'
# s_b = "1234"
# num = 1234
# print(type(s_b))
# print(type(num))
# s = 'arthur'
#
# print(len(s))
# print(s[0])
# print(s[4])
# print(s[-1])

# what is the relation between len and largest index
# print(s[len(s) - 1])

s = 'abc' # immutable
# s[1] = 'w'

# string concatenation
# s1 = 'ab'
# s2 = 'bc'
# s3 = s1 + s2 + s1
# print(s3)

print('a' * 10)
