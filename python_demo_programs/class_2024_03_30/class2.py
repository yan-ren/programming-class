# s1 = 'abc123'
# s2 = 'hello'
#
# print(len(s1))
# print(len(s2))
# print(s1[0])
# s3 = s1[0:3]
# print(s3)
# print(s1)

# weight = int(input('Please enter your weight:'))
# height = float(input('Please enter your height:'))
# BMI = weight / (height**2)
# print(BMI)

# a = 4
# b = 3
# if a > b:
#     print('a is bigger')
# else:
#     print('b is bigger')

# first = int(input('Please enter the first number'))
# second = int(input('Please enter the second number'))
# if first > second:
#     print("first number is bigger")
# elif second > first:
#     print("second number is bigger")
# else:
#     print("Two numbers are equal")

'''
Take one number from user, check positive, negative, or zero
'''
'''
Take three distinct numbers from user, find the largest one
'''
# first = int(input('enter the first number:'))
# second = int(input('enter the second number:'))
# third = int(input('enter the third number:'))
# if first > second:
#     if first > third:
#         print('first number is the largest')
#     else:
#         print('third number is the largest')
# else:
#     if second > third:
#         print('second number is the largest')
#     else:
#         print('third number is the largest')

# if first > second and first > third:
#     print('first number is the largest')
# elif second > first and second > third:
#     print('second number is the largest')
# else:
#     print('third number is the largest')

number = int(input('Please enter a number:'))
if number > 0:
    print('positive')
    if number % 2 == 0:
        print('even')
    else:
        print('odd')
elif number < 0:
    print('negative')
else:
    print('zero')

