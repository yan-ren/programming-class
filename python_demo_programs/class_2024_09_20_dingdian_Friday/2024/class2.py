'''
import turtle

window = turtle.Screen()

t = turtle.Turtle()

color = input('enter a color for drawing:')
t.fillcolor(color)

t.begin_fill()
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
t.end_fill()

turtle.done()
'''

# a = True
# print(type(a))
# b = False
# print(type(b))

a = 1
b = 1
c = 2
print(a == b)
print(a != c)
print(a > b)
print(a >= b)
print(a < b)
print(a <= b)

# not and or
a = True
print(not a)
b = False
print(a and b) # as long as we have one False, overall is False
c = True
print(a and c)

# or: as long as we have one true, overall is True
print(a or b)
print(a or c)
d = False
print(b or d)

# conditional
first = int(input('Enter the first number:'))
second = int(input('Enter the second number:'))
if first > second:
    print('First number is bigger')
else:
    print('Second number is bigger')