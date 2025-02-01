# import turtle
#
# window = turtle.Screen()
# window.setup(800, 800)
#
# t = turtle.Turtle()
#
# color = window.textinput('Enter a color:', 'red, yellow, blue').lower()
# t.fillcolor(color)
# shape = window.textinput('Enter a shape:', 'triangle, circle').lower()
#
# if shape == 'triangle':
#     t.begin_fill()
#     t.forward(100)
#     t.left(120)
#     t.forward(100)
#     t.left(120)
#     t.forward(100)
#     t.left(120)
#     t.end_fill()
# elif shape == 'circle':
#     t.begin_fill()
#     t.circle(50)
#     t.end_fill()
# else:
#     print('Shape not supported')
#
# turtle.done()

# name = input('Enter your name:')
# print('Welcome', name)
# age = int(input('Enter your age:'))
# print('Next year, you are', age + 1)

# food = input('What do you like to eat')
# while True:
#     if food == 'banana':
#         # indentation
#         print('Monkey likes it as well')
#         break
#     elif food == 'apple':
#         print('Apple is good')
#         break
#     elif food == 'orange':
#         print('Orange is not good')
#         break
#     else:
#         print('Not known')

a = 1
b = 2
res = b > a
print(res)
print(type(res)) # type is boolean
res = b < a
print(res)
print(type(res))

print(b == a)
print(b != a)

a = 'abc'
print(a == 'bc')

# if b > a:
#     print('b is bigger')



