'''
variable
- type: integer, float, boolean, string

integer/float: math (+-*/,//,%)
boolean: True/False, conditional, comparison operator(and,or,not)
string: quote
'''
# a = False
# b = False

# and operator: as long as one value is False, overall result is False
# c = a and b
# print(c)

# or operator: as long as one value is True, overall result is True
# c = a or b
# print(c)

# not operator: reverse
# c = not a
# print(c)

# s = 'Arthur' # each letter in string has index, index starts from 0
# print(s[0])
# print(len(s)) rthur' # each letter in string has index, index starts from 0
# print(s[0])
# print(len(s)) # length of string, the number of characters in the string

# string has index, from 0 to len() - 1,
# question: how to loop through each letter in string using while loop
# i = 0
# while i < len(s):
#     print(s[i])
#     i += 1

# exercise: how to print the string reversely using while loop
# i = len(s) - 1
# while i >= 0:
#     print(s[i])
#     i -= 1

# palindrome: a word that read the same from left to right and right to left
# e.g. kayak
# s = 'abc'
# s_reverse = ''
#
# i = len(s) - 1
# while i >= 0:
#     s_reverse = s_reverse + s[i]
#     i -= 1
#
# print(s_reverse)

# import turtle
#
#
# screen = turtle.Screen()
# screen.setup(600, 800)
#
# pen = turtle.Turtle()
#
# word = screen.textinput('Input', 'Enter a word for palindrome checking:')
# word_reverse = ''
# # TODO: write program to create word_reverse
# i = len(word) - 1
# while i >= 0:
#     word_reverse = word_reverse + word[i]
#     i -= 1
#
# if word == word_reverse:
#     pen.write('Congrats, you find a palindrome', align='center', font=('Arial', 24, 'bold'))
# else:
#     pen.write('Unfortunately, this is not a palindrome', align='center', font=('Arial', 24, 'bold'))
#
# turtle.done()

# s = 'abcdefghijk'
# print(type(s))
# print(len(s))
# print(s[0])
# print(s[1])
# print(s[2])
#
# i = 0
# while i < len(s):
#     print(s[i])
#     i += 1

# how do you calculate the sum from 1 to 10, e.g. 1+2+3+4+5+ ... +10
# i = 1
# s = 0
# while i <= 10:
#     s = s + i
#     i += 1
#
# print(s)

num1 = int(input('Enter the first value:'))
num2 = int(input('Enter the second value:'))

s = 0
i = num1
while i <= num2:
    s = s + i
    i += 1

print("The sum from " + str(num1) + " to " + str(num2) + " is " + str(s))

'''
use input(), while loop
create a program that print all even number under a uer input
e.g. if user type: 10
you should print 2, 4, 6, 8
'''


