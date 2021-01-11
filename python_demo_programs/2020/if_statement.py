# check if a number is odd or even
# number = int(input('enter a number:'))
#
# if number % 2 == 0:
#     print(number, 'is even')
# else:
#     print(number, 'is odd')

number1 = int(input('enter the first number'))
number2 = int(input('enter the second number'))
number3 = int(input('enter the third number'))

average = (number1 + number2 + number3)/3
if average > 60:
    print('good score')
else:
    print('not good')