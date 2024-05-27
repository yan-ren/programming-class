s = 'Arthur'

print(s[1:5:2])
print(s[5::-1])

# number = int(input('Enter a number:'))
# if number > 0:
#     print('The number is positive')
# elif number < 0:
#     print('The number is negative')
# else:
#     print('The number is zero')
#
# if number % 2 == 0:
#     print('The number is even')
# else:
#     print('The number is odd')

a = int(input('Enter first number:'))
b = int(input('Enter second number:'))
c = int(input('Enter third number'))

# how to find out the largest from a, b, c
if a > b and a > c:
    print('a is the largest')
elif b > a and b > c:
    print('b is the largest')
else:
    print('c is the largest')

# exercise: how to rewrite above program(24-28) using nested if statement