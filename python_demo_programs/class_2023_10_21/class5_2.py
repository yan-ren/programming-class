'''
Ask user to enter three scores(integer),
calculate the average score and tell user if average is above 60
'''

number1 = int(input('enter the first number'))
number2 = int(input('enter the second number'))
number3 = int(input('enter the third number'))

average = (number1 + number2 + number3) / 3
print(average)

if average > 60:
    print('average is above 60')
else:
    print('average is not above 60')