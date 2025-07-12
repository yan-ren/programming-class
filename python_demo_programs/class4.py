'''
last time:

if statement: if elif else

control flow:
1. conditional -> if statement
2. loop
 - while
 - for

Today: Topic 5 - slide 05


'''
# exercise: take three number from user, find the largest number
# can assume three numbers are different
# first = int(input('Enter the first number:'))
# second = int(input('Enter the second number:'))
# third = int(input('Enter the third number:'))
#
# # nested if statement
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
#
#
# # solution 2
# if first > second and first > third:
#     print('First number is the largest')
# elif second > first and second > third:
#     print('Second number is the largest')
# else:
#     print('Third number is the largest')

# i = 0
# while i < 10:
#     print('Hello')
#     print(i)
#     # i = i + 1
#     i += 1

# write code to print from 10 to 1 using while loop
# i = 10
# while i > 0:
#     print(i)
#     # i = i - 1
#     i -= 1

# calculate the sum from 1 to 100
# 1 + 2 + 3 + ... + 100
# i = 1
# s = 0
# while i <= 100:
#     i += 1
#     s = s + i
#
# print(s)

# how to print all even number under 50
# i = 2
# while i < 50:
#     print(i)
#     i += 2

# i = 1
# while i < 50:
#     if i % 2 == 0:
#         print(i)
#     i += 1

i = 0
while i < 5:
    j = 0
    while j < i:
        print(j)
        j += 1
    i += 1

'''
exercise 1:
print squares of numbers from 1 to 10
1 4 9 16 25 36 49 64 81 100

exercise 2:
print odd numbers from 1 to 20

exercise 3:
Find the smallest number that is divisible by both 3 and 5 over 100
start from 100, find and print the first number greater than 100 that is divisible by both 3 and 5
'''