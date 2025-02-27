# exercise 1: ask user for two numbers, determine which is bigger
# first = int(input('Enter the first number:'))
# input takes everything as string, '12' -> 12
# second = int(input('Enter the second number:'))
#
# if first > second:
#     print('First number is bigger')
# elif second > first:
#     print('Second number is bigger')
# else:
#     print('Same')

# exercise 2: ask user for three numbers, determine the biggest one, assume all numbers are different
# first = int(input('Enter the first number:'))
# second = int(input('Enter the second number:'))
# third = int(input('Enter the third number:'))

# solution1
# if first > second > third:
# if first > second and first > third:
#     print('First number is the biggest')
# elif second > first and second > third:
#     print('Second number is the biggest')
# else:
#     print('Third number is the biggest')

# solution2
# nested if statement
# if first > second:
#     if first > third:
#         print('First number is the biggest')
#     else:
#         print('Third number is the biggest')
# else:
#     if second > third:
#         print('Second number is the biggest')
#     else:
#         print('Third number is the biggest')

'''
Create a chat game using

1. input(): get user's answer and option
2. if elif else ...
'''

print('Welcome to the door choosing game, there are two doors in front of you')
print('Do you choose door 1 or door 2?')

door = input('Your choice:')

if door == '1':
    print('There is a bear eating cake, what do you do?')
    print('Option 1: take the cake')
    print('Option 2: scream at the bear')

    option = input('Your choice:')

    if option == '1':
        print('Bear eats your leg')
    elif option == '2':
        print('Bear eats your face')
    else:
        print('Run away')
elif door == '2':
    pass