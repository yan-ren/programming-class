# print(1 == 1) # compare equal
# print(1 != 2) # compare not equal

# print(1 + 1)

# boolean operation
# and operator: if one side is false overall is false
# a = True
# b = False
#
# print(a and b)

# print(True and True)
# print(True and False)
# print(False and True)
# print(False and False)

# or operator: if one side is true, overall is true
# print(True or True)
# print(True or False)
# print(False or True)
# print(False or False)

# not operator: reverse
# print(not True)
# print(not False)

# if statement
first = int(input('Enter the first number:'))
second = int(input('Enter the second number:'))

if first > second:
    print('First number is larger')
elif second > first:
    print('Second number is larger')
else:
    print('Both are same')

# question: there is a logic problem in above code, meaning it's not 100% correct

# write a similar program: ask user for a number, tell them if it's positive, negative or zero
number = int(input('Enter a number:'))
if number > 0:
    print('Positive')
elif number < 0:
    print('Negative')
else:
    print('Zero')

# question: how to check a number is even or odd?
# in math if a number is even, it can be divided by 2, meaning divided by 2 there are no remainder
if number % 2 == 0:
    print('Even')
else:
    print('Odd')

'''
Write a program asking user for three numbers, assume all those are different
How to find out the largest one?
'''
first = int(input('Enter the first number:'))
second = int(input('Enter the second number:'))
third = int(input('Enter the third number:'))

