# first = int(input('first number:'))
# second = int(input('second number:'))
#
# if first > second:
#     print("condition is true")
#     print("first number is bigger")
#
# print("program finish")
import math

# a = int(input('please enter a number:'))
#
# if a > 0:
#     print('number is positive')
# elif a < 0:
#     print('number is negative')
# else:
#     print('number is zero')

# a = 1
# b = 2
# print(a+b)
# print(a**b)
#
# print(math.sqrt(2))

# first = int(input('enter first number:'))
# second = int(input('enter second number:'))
# third = int(input('enter third number:'))

# if first > second:
#     if first > third:
#         print('first is the largest')
#     else:
#         print('third is the largest')
# else:
#     if second > third:
#         print('second is the largest')
#     else:
#         print('third is the largest')

# if first > second and first > third:
#     print('first is the largest')
# elif second > first and second > third:
#     print('second is the largest')
# else:
#     print('third is the largest')

print('You enter a dark room with two doors, do you go through door 1 or door 2:')
door = input('your choice:')

if door == '1':
    print('There is a giant bear here eating lunch, what do you do:')
    print('1. run away')
    print('2. scream at the bear')

    option = input('your option:')

    if option == '1':
        print('The bear eats your face off')
    elif option == '2':
        print('The bear eats your legs off')

# elif door == '2':
#
# else:
