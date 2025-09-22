s = 'Arthur'
print(s[1])
print(len(s))
print(s[5])
print(s[len(s) - 1])

print(s[0:2])

number = int(input('Enter a number'))
if number > 0:
    print('Positive')
else:
    print('Non positive')


number1 = int(input('Enter the first number:'))
number2 = int(input('Enter the second number:'))

if number1 > number2:
    print('First number is bigger')
elif number1 < number2:
    print('Second number is bigger')
else:
    print('Same')

# if there is number3, how to find the biggest?