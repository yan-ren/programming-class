# number = int(input('enter a number to check positive: '))
#
# if number > 0:
#     print('number is positive')
# elif number < 0:
#     print('number is negative')
# else:
#     print('number is zero')


# number = int(input('enter a number to check even or odd: '))
#
# if number % 2 == 0:
#     print('number is even')
# else:
#     print('number is odd')

people = 30
cars = 40
trucks = 15

# if cars > people:
#     print('we should take the cars')
# elif cars < people:
#     print('we should not take the cars')
# else:
#     print('we cannot decide')

# if people > (trucks + cars):
#     print('we can take cars or trucks')

# a = int(input('enter the first value:'))
# b = int(input('enter the second value:'))
# c = int(input('enter the third value:'))

# if a > b:
#     if a > c:
#         print(a, 'is the biggest')
#     else:
#         print(c, 'is the biggest')
# else:
#     if b > c:
#         print(b, 'is the biggest')
#     else:
#         print(c, 'is the biggest')

# if a > b and a > c:
#     print(a, 'is the biggest')
# elif b > a and b > c:
#     print(b, 'is the biggest')
# elif c > a and c > b:
#     print(c, 'is the biggest')

'''
Decision game
'''
# print('You enter a dark room with two doors, do you pick door 1 or door 2:')
# door = input('you pick:')
#
# if door == '1':
#     print('There is a bear eating food, what do you do')
#     print('1. take the food')
#     print('2. scream')
#
#     option = input('your option:')
#     if option == '1':
#         print('something')
#     elif option == '2':
#         print('something')
#     else:
#         print('')
#
# elif door == '2':
#     print('')

'''
Ask user to enter three scores(integer), 
calculate the average score and tell user if average is above 60
'''
score_1 = int(input('enter first score:'))
score_2 = int(input('enter second score:'))
score_3 = int(input('enter third score:'))
number_of_score = 3

avg = (score_1 + score_2 + score_3) / number_of_score
if avg > 60:
    print('pass')
else:
    print('fail')