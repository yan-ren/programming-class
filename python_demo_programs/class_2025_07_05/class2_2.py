# import turtle
#
# window = turtle.Screen()
# window.setup(800, 800)
# pen = turtle.Turtle()
#
# pen.forward(100)
# pen.left(90)
# pen.forward(100)
# pen.left(90)
# pen.forward(100)
# pen.left(90)
# pen.forward(100)
# pen.left(90)
#
# pen.forward(80)
# pen.left(90)
# pen.forward(80)
# pen.left(90)
# pen.forward(80)
# pen.left(90)
# pen.forward(80)
# pen.left(90)
#
# turtle.done()

'''
variable

int
float
boolean
string
'''
# x = 5
# y = 3
# print(type(x))
# print(x + y)
# print(x - y)
# print(x * y)
# print(x / y) # float division
# print(x // y) # integer division
#
# print(x ** y)
# print(x % y) # mod

# a = True
# b = False
# print(type(a))
# x = 5
# y = 4
# z = 6
# print(x > y > z)
# print(x < y)
# print(x == y)
# print(x >= y)
# print(x != y)

# s = '123'
# n = 123
# print('hello')

# name = input('What is your name:')
# print(type(name))
# print('Welcome', name)

celsius = int(input('Enter degree celsius:'))
fahrenheit = celsius * 9 / 5 + 32
print(fahrenheit)

# ask for kilometer and covert to miles

'''
1. How many seconds are there in 42 minutes 42 seconds?
2. How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in 1 mile.
3. If you run a 10 kilometers race in 42 minutes 42 seconds, what is your average speed (time per
mile in minutes and seconds)? What is your average speed in miles per hour?
'''
minutes = 40
seconds = 42
time = minutes * 60 + seconds
print(time)

distance = 10 / 1.61

speed = distance / time
