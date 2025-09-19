'''
control flow
- conditional
- loop

conditional
- if statement

'''

# number = int(input('Enter a number:'))
# if number > 0:
#     print('positive') # indentation
# elif number < 0:
#     print('negative')
# else:
#     print('zero')


# number = 120
#
# # logical error
# if number > 1:
#     print('number is bigger than 1')
# elif number > 10:
#     print('number is bigger than 10')
# elif number > 100:
#     print('number is bigger than 100')
#
# # fix
# if number > 100:
#     print('number is bigger than 100')
# elif number > 10:
#     print('number is bigger than 10')
# elif number > 1:
#     print('number is bigger than 1')

# number1 = int(input('Enter the first number:'))
# number2 = int(input('Enter the second number:'))
#
# if number1 > number2:
#     print('First number is bigger')
# elif number1 < number2:
#     print('Second number is bigger')
# else:
#     print('Same')

# number = int(input('Enter a number:'))
#
# if number % 2 == 0:
#     print('Even')
# else:
#     print('Odd')

number1 = int(input('Enter the first number:'))
number2 = int(input('Enter the second number:'))
number3 = int(input('Enter the third number:'))

# nested if statement
if number1 > number2:
    if number1 > number3:
        print('First number is the largest')
    else:
        print('Third number is the largest')
else:
    if number2 > number3:
        print('Second number is the largest')
    else:
        print('Third number is the largest')

# option2
if number1 > number2 and number1 > number3:
    print('First number is the largest')
elif number2 > number1 and number2 > number3:
    print('Second number is the largest')
else:
    print('Third number is the largest')

