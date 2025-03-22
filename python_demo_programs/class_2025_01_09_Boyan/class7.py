'''
loop - repeat

- for loop
- while loop
'''
# i = 0
#
# while i < 10: # loop header
#     print(i) # loop body
#     i = i + 1

# exercise: how to print from 10 to 1 using while loop
# import time
#
#
# i = 10
#
# while i > 0: # loop header
#     print(i) # loop body
#     i = i - 1
#     time.sleep(1)

# calculate the sum of all numbers under 100
# i = 1
# s = 0
# while i <= 100:
#     s = s + i
#     i += 1 # i = i + 1
#
# print(s)

# example: print all even number under 20
# number = 2
# while number <= 20:
#     print(number)
#     number += 2
#
#
# number = 1
# while number <= 20:
#     if number % 2 == 0:
#         print(number)
#
#     number += 1

# import turtle
#
# screen = turtle.Screen()
# screen.setup(800, 600)
#
# pen = turtle.Turtle()
#
# # draw a square
# # nested loop
# j = 0
# while j < 4:
#     i = 0
#     while i < 4:
#         pen.forward(100)
#         pen.left(90)
#         i += 1
#
#     pen.left(15)
#     j += 1
#
# turtle.done()

'''
Using while loop and input() function to write a even odd number checker
e.g, the program should run like following:

Please Enter Number: 7
7 is a odd number
6 is a even number
5 is a odd number
4 is a even number
3 is a odd number
2 is a even number
1 is a odd number
'''

# number = int(input('Please Enter Number:'))
# while number > 0:
#     if number % 2 == 0:
#         print(number, 'is an even number')
#     else:
#         print(number, 'is an odd number')
#
#     number -= 1
