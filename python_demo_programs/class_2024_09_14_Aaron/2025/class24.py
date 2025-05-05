import turtle

color_dict = {
    'red': '#FF0000',
    'blue': '#0000FF',
    "green": "#00FF00",
    "yellow": "#FFFF00",
    "purple": "#800080",
    "orange": "#FFA500"
}

screen = turtle.Screen()
pen = turtle.Turtle()
pen.pensize(5)
pen.speed(1)

print('Available color:')
for color in color_dict:
    print('-', color)

chosen_color = input('Choose a color for the turtle to draw with: ').lower()

if chosen_color in color_dict:
    pen.color(color_dict[chosen_color])
    # draw a happy face
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
    # mouth
    pen.penup()
    pen.goto(-40, -20)
    pen.setheading(-60)
    pen.pendown()
    pen.color('black')
    pen.circle(50, 120)

screen.exitonclick()


grade_book = {}
while True:
    name = input('Enter student name (or type "done" to finish): ')
    if name.lower() == 'done':
        break
    grade = int(input(f'Enter grade for {name}'))
    grade_book[name] = grade

# print the grade book
for student, grade in grade_book.items():
    print(student, grade)

# exercise: find who has the highest grade
top_student = None
top_grade = -1


'''
Create a dictionary with names and phone numbers. 
Ask the user to enter a name and show the phone number.
'''
phone_book = {
    "Alice": "123-456-7890",
    "Bob": "555-123-4567",
    "Charlie": "987-654-3210"
}
