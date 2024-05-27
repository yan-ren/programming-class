'''
You get three numbers from user input, find which one is the largest
'''
# a = int(input('enter the first number:'))
# b = int(input('enter the second number:'))
# c = int(input('enter the third number:'))
#
# # solution 1
# if a > b and a > c:
#     print('a is the largest')
# elif b > a and b > c:
#     print('b is the largest')
# else:
#     print('c is the largest')
#
# # solution 2, nested if statement
# if a > b:
#     if a > c:
#         print('a is the largest')
#     else:
#         print('c is the largest')
# else:
#     if b > c:
#         print('b is the largest')
#     else:
#         print('c is the largest')

# let's write a simple decision game, using input and if statement
print('You enter a dark room with two doors. do you go through door 1 or door 2')

door = input('>')

if door == '1':
    print('There is a giant bear here eating a cheese cake')
    print('What do you do')
    print('1. take the cake')
    print('2. scream at the bear')

    bear = input('>')

    if bear == '1':
        print('The bear eats your face off')
    elif bear == '2':
        print('The bear eats your legs off')
    else:
        print('Bear runs away')
# elif door == '2':
