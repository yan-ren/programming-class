'''
if statement
while loop
'''
# tom_pass = 'tom123'
# jerry_pass = 'jerry123'
#
# password = input('Enter a password:')
#
# if password == tom_pass:
#     print('Welcome Tom')
# elif password == jerry_pass:
#     print('Welcome Jerry')
# else:
#     print('Unrecognized')

# import turtle
#
# tom_pass = 'tom123'
# jerry_pass = 'jerry123'
#
# screen = turtle.Screen()
# t = turtle.Turtle()
# t.speed(0)
# t.hideturtle()
#
# while True:
#     password = screen.textinput('Login', 'Enter password:')
#
#     if password == tom_pass:
#         t.clear()
#         t.color('green')
#         t.begin_fill()
#         t.circle(50)
#         t.end_fill()
#         screen.title('Welcome Tom')
#         break
#     elif password == jerry_pass:
#         t.clear()
#         t.color('blue')
#         t.begin_fill()
#         t.circle(50)
#         t.end_fill()
#         screen.title('Welcome Jerry')
#         break
#     else:
#         t.clear()
#         t.color('red')
#         t.forward(50)
#         t.backward(100)
#         t.forward(50)
#         screen.title('Wrong password')
#
# turtle.done()

'''after class
- based on above program, create your password
'''
# number = 1
#
# while number < 100:
#     print(number)
#     number = number + 1

# number = 100
# while number > 0:
#     print(number)
#     number = number - 1

sum = 0
number = 1

while number <= 100:
    sum = sum + number
    number = number + 1

print(sum)