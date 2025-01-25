'''
Basic Types

integer
float
string
boolean - conditional
'''

# a = 1
# print(type(a))
# b = 2
# print(type(b))
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b) # float division
# print(a // b) # integer division
# print(a ** b)
# print(7 % 3)
# print(5 % 2)
#
# s = '12'
# print(s + '1')

# value = input('Enter something:')
# print('you entered', value)
# print(type(value))

# (0°C × 9/5) + 32 = 32°F

# temperature = input('Enter the temperature in celsius: ')
#
# for ch in temperature:
#     if ch.isalpha():
#         print('there is an letter in temperature')
#         exit(0)
#
# print('Temperature in Fahrenheit', int(temperature) * 9 / 5 + 32)
#
# if int(temperature) > 40:
#     print('high temperature')
# else:
#     print('low temperature')

# import turtle
#
# window = turtle.Screen()
# window.setup(800, 800)
#
# t = turtle.Turtle()
# t.fillcolor('red')
#
# t.begin_fill()
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.end_fill()
#
# t.penup()
# t.goto(200, 200)
# t.pendown()
#
# t.fillcolor('green')
# t.begin_fill()
# t.circle(50)
# t.end_fill()
#
# turtle.done()

temperature = 50
result = temperature > 40
print(type(result))

a = True
b = False
print(type(a))
print(type(b))

