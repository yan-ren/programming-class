'''
boolean: True False
'''
# a = True
# b = False
#
# print(type(a))
# print(type(b))
#
# print(1 == 1)
# print(2 * 3 == 5)

a = True
print(not a)

a = 2
print(not(not(a == 3)))

# and
print(True and True)
print(True and False)
print(False and True)
print(False and False)

# or
print(True or False)
print(True or True)
print(False or True)
print(False or False)

print(not False or True)

a = 2
b = 1
if a > b:
    print('a is bigger')
elif a < b:
    print('')
else:
    print('a is not bigger')

# ask a number from user, tell them it's positive negative or zero

# ask a number form user, tell them it's even or odd
# number = int(input('Enter a number:'))
# if number % 2 == 0:
#     print('Even')
# else:
#     print('Odd')

# ash user for three number, tell them which one is the largest
first = int(input('First:'))
second = int(input('Second:'))
third = int(input('Third:'))
# if first > second > third:
if first > second:
    if first > third:
        print('first is largest')
    else:
        print('third is largest')
else:
    if second > third:
        print('second is largest')
    else:
        print('third is largest')

# nested if statement
# Ask for a score 0–100 and print:
# A: 90+
# B: 80–89
# C: 70–79
# D: 60–69
# F: below 60

# Ask for a year.
# A leap year is divisible by 4 but not 100,
# unless it's also divisible by 400.