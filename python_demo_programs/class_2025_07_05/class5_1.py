# Use a while loop to ask the user to enter 5 numbers. After that, print the total sum
# and average

# i = 0
# s = 0
# while i < 5:
#     s += int(input('Enter a number:'))
#     i += 1
#
# print(s)
# print(s/5)

# import turtle
#
# wn = turtle.Screen()
# wn.setup(800, 600)
#
# pen = turtle.Turtle()
#
# angle = 15
# j = 0
# while j < 360 / angle:
#     i = 0
#     while i < 4:
#         if i == 0:
#             pen.color('red')
#         elif i == 1:
#             pen.color('yellow')
#         elif i == 2:
#             pen.color('green')
#         elif i == 3:
#             pen.color('blue')
#         pen.forward(100)
#         pen.left(90)
#         i += 1
#     pen.left(angle)
#     j += 1
#
# turtle.done()

# break, continue
# i = 0
# while i < 5:
#     if i == 2:
#         i += 1
#         continue
#     print(i)
#     i += 1

j = 0
while j < 4:
    i = 0
    while i < 4:
        print('*', end='')
        i += 1
    print()
    j += 1

'''
*
**
***
****

Write a loop that calculates the total of the following series of numbers:
(1 / 50) + (2 / 49) + (3 / 48) + (4 / 47) + ...+ (48 / 3) + (49 / 2) + (50 / 1)
'''