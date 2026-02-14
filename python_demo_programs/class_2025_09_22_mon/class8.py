# review while loop
# i = 0
# while i < 10: # loop header
#     print(i)  # loop body
#     i += 1

# exercise: print all even number under 50
# option 1
# i = 2
# while i < 50:
#     print(i)
#     i += 2

# option 2
# i = 1
# while i < 50:
#     if i % 2 == 0:
#         print(i)
#     i += 1

# exercise: calculate the sum of 2 + 4 + 6 + 8 + ... + 98 + 100
# i = 1
# s = 0
# while i <= 100:
#     if i % 2 == 0:
#         s += i
#     i += 1

'''
build a countdown counter, ask user for a number, after entering the number, show the countdown from the given number to zero

using turtle, while loop
'''
import turtle
import time

window = turtle.Screen()
window.setup(800, 800)

pen = turtle.Turtle()
pen.hideturtle()

start = int(window.numinput('Enter a number', 'Enter a number for counting down'))

while start >= 0:
    pen.clear()
    pen.write(start, align='center', font=('Arial', 24, 'bold'))
    time.sleep(1)
    start -= 1

turtle.done()

'''
follow up:
improve count down program
'''