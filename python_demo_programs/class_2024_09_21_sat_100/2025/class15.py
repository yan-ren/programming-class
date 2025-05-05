'''
1. Count Word Occurrences
Write a program that asks the user for a sentence and counts how many times each word appears.
and print the most frequent word

Input: "cat dog cat"
Output: {'cat': 2, 'dog': 1}
'''
# sentence = input('Enter a sentence:')
# words = sentence.split()
#
# word_count = {}
#
# for word in words:
#     if word in word_count:
#         word_count[word] += 1
#     else:
#         word_count[word] = 1
#
# print(word_count)

import turtle

color_dict = {
    "red": "#FF0000",
    "blue": "#0000FF",
    "green": "#00FF00",
    "yellow": "#FFFF00",
    "purple": "#800080",
    "orange": "#FFA500"
}

screen = turtle.Screen()
screen.title('Turtle Color Selector')
pen = turtle.Turtle()
pen.pensize(5)
pen.speed(1)

print('Available colors:')
for color in color_dict:
    print('-', color)

chosen_color = input('Choose a color for the turtle to draw with:').lower()

if chosen_color in color_dict:
    pen.color(color_dict[chosen_color])
    # face
    pen.penup()
    pen.goto(0, -100)
    pen.pendown()
    pen.begin_fill()
    pen.circle(100)
    pen.end_fill()
    # eyes
    pen.penup()
    pen.goto(-30, 30)
    pen.dot(20, 'black')
    pen.goto(30, 30)
    pen.dot(20, 'black')
    # smile
    pen.penup()
    pen.goto(-40, -20)
    pen.setheading(-60)
    pen.pendown()
    pen.color('black')
    pen.circle(50, 120)

screen.exitonclick()

'''puzzle program

Create a dictionary of 5 countries and their capitals.

Ask the user 3 random questions like: “What is the capital of ___?”

If the answer is correct, say “✅ Correct!” — if not, show the right answer.

Show the final score out of 3.
'''