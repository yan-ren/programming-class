'''
Today: build a decision game
- input()
- if elif else ...
'''

print('Welcome to the door choosing game, there are two doors in front of you')
print('Do you choose door 1 or door 2')

door = input('Your choice:')

if door == '1':
    print('There is a bear eating cake, what do you do?')
    print('Option 1: take the cake')
    print('Option 2: screaming')

    option = input('Your choice:')
    if option == '1':
        print('Bear eats your face')
    elif option == '2':
        print('Bear eats your leg')
    else:
        print('Run away')
elif door == '2':
    pass
else:
    print('Invalid option, game over')










# exercise 1: ask user for two numbers, determine which is bigger

# num1 = int(input('Enter the first number:'))
# num2 = int(input('Enter the second number:'))
#
# if num1 > num2:
#     print('first number is bigger')
# elif num1 < num2:
#     print('second number is bigger')
# else:
#     print('same')

# exercise 2: ask user for three numbers, determine the biggest one
# num1 = float(input('first:'))
# num2 = float(input('second:'))
# num3 = float(input('third:'))
#
# if num1 > num2:
#     if num1 > num3:
#         print('first is the biggest')
#     else:
#         print('third is the biggest')
# else:
#     if num2 > num3:
#         print('second is the biggest')
#     else:
#         print('third is the biggest')

# if num1 > num2 > num3
# if num1 > num3 > num2
# if num1 > num2 and num1 > num3:
#     print('first is the biggest')
# elif num2 > num1 and num2 > num3:
#     print('second is the largest')
# else:
#     print('third is the largest')

