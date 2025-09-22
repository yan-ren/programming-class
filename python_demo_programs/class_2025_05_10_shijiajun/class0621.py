# if there is number3, how to find the biggest?
#
# number1 = int(input('Enter the first number:'))
# number2 = int(input('Enter the second number:'))
# number3 = int(input('Enter the third number:'))

# if number1 > number2:
#     if number1 > number3:
#         print('first number is largest')
#     else:
#         print('third number is largest')
# else:
#     if number2 > number3:
#         print('second number is largest')
#     else:
#         print('third number is largest')

# if number1 > number2 and number1 > number3:
#     print('')
# elif number2 > number1 and number2 > number3:
#     print('')
# else:
#     print('')

# number = int(input('Enter a number:'))
#
# if number % 2 == 1:
#     print("odd number")
# else:
#     print('even number')

# import turtle
#
#
# t = turtle.Turtle()
# t.shape('turtle')
# t.speed(1)
# t.penup()
#
# screen = turtle.Screen()
#
# def go_left_or_right(x, y):
#     if x < 0:
#         t.color('blue')
#         t.setheading(180)
#         t.forward(50)
#     else:
#         t.color('green')
#         t.setheading(0)
#         t.forward(50)
#
# screen.onclick(go_left_or_right)
#
# screen.mainloop()

'''
Ask for a student's score (0–100). Print their grade:
A: 90+
B: 80–89
C: 70–79
D: 60–69
F: below 60
'''

score = int(input("Enter your score: "))

# TODO: Add if-elif-else logic to print grade