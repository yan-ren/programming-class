import numbers
from re import T


def function1():
    print('we are in function1')


# call the function1
# function1()
# function1()

# wirte a function, inside: ask user's name and print welcome message
# def welcome():
#     name = input("what's your name?")
#     print('welcome ' + name)

# welcome()

# def welcome(first_name, last_name):
#     print('welcome ' + name1)
#     print('welcome ' + name2)


# welcome('mike', 'denis')

# write a function that takes a list as input and print each value in list using loops
# def print_list(l):
#     for value in l:
#         print(value)

# return is a keyword that can be used in function to return value to the outside
# def max_value(l):
#     max = l[0]
#     for number in l:
#         if number > max:
#             max = number
    
#     return max


# res = max_value([1, 2, 4, 3, 5])
# res = max_value([3, 1, 4])
# print(res)

def is_even(number):
    if number % 2 == 0:
        return True
    return False


number = int(input('enter a number'))
if is_even(number):
    print('number is even')
else:
    print('number is odd')

