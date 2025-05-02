# a = 1
# b = 2
#
# print(a - b)
# print(a + b)
# print(a * b)
# print(a / b) # float division -> float -> number with decimal points
# print(a // b) # integer division -> integer -> number without decimal points
# print(5 % 3) # module -> reste de la division
# print(2**5)


import turtle

screen = turtle.Screen()
screen.setup(800, 600)

pen = turtle.Turtle()

name = screen.textinput('Input', "What's your name:")
pen.write('Welcome ' + name, align='center', font=('Arial', 24, 'bold'))

num1 = screen.numinput('Input', 'Enter the first number:')
num2 = screen.numinput('Input', 'Enter the second number:')

pen.clear()
pen.write(str(num1) + "+" + str(num2) + "=" + str(num1 + num2), align='center', font=('Arial', 24, 'bold'))
turtle.done()
