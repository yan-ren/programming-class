# '''
# string & turtle race game
#
# int, float
# boolean: True False
# '''
# a = True
# b = False
# print(type(a))
# print(type(b))
#
# # boolean coming from comparison
# print(2 > 1)
# print(2 > 3)
# print(2 < 3)
# print(2 == 3)
# print(2 != 3)
#
# first = int(input('Enter the first value:'))
# second = int(input('Enter the second value:'))
#
# if first > second:
#     print('First value is bigger')
# elif second > first:
#     print('Second value is bigger')
# else:
#     print('same')
#
# python string: using single or double for characters
# s = 'abcde'
# t = "123abc"
# print(type(s))
# print(type(t))
# t = 'asdfa1234!@#$%^ '
# name = 'Arthur'
# # access each character by index
# print(name[1])
# print(name[5])
# # print(name[6])
# print(len(name))
# # access the last char
# print(name[5])
# print(name[len(name) - 1])
#
# # string concatenation
# a = 'hello'
# b = 'world'
# c = a + b + a
# print(a * 10)
# print(c)

# t = 'Arthur'

# slicing: cut pieces from string
# print(t[1:3])
# print(t.lower())
# print(t.upper())
#
# if 'ur' in t:
#     print('yes')

import random
import turtle

# List of words and hint
words = [
    ('piano', 'I have black and white keys but cannot open doors'),
    ('giraffe', 'I am the tallest land animal'),
    ('moon', 'I control the tides and light up the night sky'),
    ("shadow", "I follow you everywhere but have no substance."),
    ("clock", "I have hands but cannot clap.")
]

# pick a random word and hint
word, hint = random.choice(words)

screen = turtle.Screen()

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.goto(0, 50)
pen.write("🔍 Guess the Word!", align="center", font=("Arial", 24, "bold"))

pen.goto(0, 0)
pen.write(f"Hint: {hint}", align="center", font=("Arial", 18, "italic"))

guess = screen.textinput('Your guess', 'Enter your guess:').lower()

pen.goto(0, -50)
if guess == word:
    pen.write("🎉😁 Correct! You guessed it right!", align="center", font=("Arial", 18, "bold"))
else:
    pen.write("❌ Wrong! The correct word was " + word, align="center", font=("Arial", 18, "bold"))

# pen.clear() to remove previous words on the screen

turtle.done()