'''
basic types:
int
float
boolean
string
'''
# a = True
# b = False
# print(type(a))
#
# print(2 > 1)
# print(2 > 3)
# print(2 >= 3)
# print(2 < 3)
# print(2 <= 3)
# print(2 == 3) # equality
# print(2 != 3) # not equal

# boolean operator
# x = True
# y = False

# print(x and y) # one side is False, overall is False
# print(x or y) # one side is True, overall is True
# print(not x) # reverse
#
# print(True and True)
# print(True and False)
# print(False and True)
# print(False and False)
#
# print(True or True)
# print(True or False)
# print(False or True)
# print(False or False)
#
# print(not True)
# print(not False)

# name = input('Enter your name:')
# print(name)
# print(type(name))

# s1 = '1'
# s2 = '2'
# print(s1 + s2) # string concatenation
# print(1 + 2)

# age = input('How old are you:')
# age = int(age)
# if age > 18:
#     print('Adult')
# else:
#     print('Under age')

# s1 = 'hello'
# s2 = 'hi'
# print(s1 > s2)
# print(len(s1))

import turtle

wn = turtle.Screen()
wn.setup(600, 800)
wn.bgcolor('lightblue')

pen = turtle.Turtle()
pen.color('red')

pen.begin_fill()
pen.forward(100)
pen.left(90)
pen.forward(100)
pen.left(90)
pen.forward(100)
pen.left(90)
pen.forward(100)
pen.left(90)
pen.end_fill()

turtle.done()