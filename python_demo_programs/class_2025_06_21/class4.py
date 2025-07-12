'''
control flow
- conditional
- loop
'''

# i = 0
# while i < 10:
#     print(i)
#     # i = i + 1
#     i += 1

# i = 10
# while i > 0:
#     print(i)
#     i -= 1

# print all even number under 20
# i = 2
# while i < 20:
#     print(i)
#     i += 2

# 1 + 2 + ... + 100 = ?
# i = 1
# s = 0
# while i <= 100:
#     s = s + i
#     i += 1
# print(s)

# 2 + 4 + 6 + ... + 100 = ?

# Print Squares of Numbers from 1 to 10
# e.g. 1 4 9 16 25 36 49 64 81 100
# i = 1
# while i <= 10:
#     print(i * i)
#     i += 1

# Use a while loop to print "Hello" exactly 5 times.

import turtle

wn = turtle.Screen()
wn.setup(600, 800)
wn.bgcolor('lightblue')

pen = turtle.Turtle()
pen.color('red')

# pen.begin_fill()
i = 0
while i < 4:
    pen.forward(100)
    pen.left(90)
    i += 1

i = 0
while i < 3:
    pen.forward(100)
    pen.left(120)
    i += 1

# pen.end_fill()

turtle.done()


'''
1. Print All Numbers from 50 to 60
2. Count Down by Twos from 20 to 0, e.g. 20 18 16 ... 0
3. Double Until Over 1000
Start with 1. Keep doubling it (multiply by 2) until the value is over 1000. Print all the values.
1 2 4 8 16 ... 
'''