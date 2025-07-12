'''
Python
1. variable: int, float, boolean, string
2. if statement
3. loop: while, for
4. function: def
5. basic data structure: list, dictionary, set?, tuple?

----
oop: class/object
data structures
algorithm
'''

for i in range(10):
    print(i)

s = 'abcde'
for c in s:
    print(c)

l = [1, 2, 3]
for number in l:
    print(number)


'''
Write a function that takes a list of numbers as input, find the max and min value in the list
without using min(), max() 
'''
# def min_max(numbers):
#     max = numbers[0] # ?
#     min = numbers[0]
#     for num in numbers:
#         if num > max:
#             max = num
#         if num < min:
#             min = num
#
#     return min, max
#
# numbers = [-1, -2, -10, -4, -20]
# print(min_max(numbers))

import turtle

window = turtle.Screen()
window.setup(800, 800)
window.bgcolor('lightblue')

ball = turtle.Turtle()
ball.shape('circle')
ball.color('red')
ball.penup()

ball.dy = 0
gravity = 0.1

while True:
    ball.dy -= gravity
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() < -400:
        ball.dy = ball.dy * -1

turtle.done()