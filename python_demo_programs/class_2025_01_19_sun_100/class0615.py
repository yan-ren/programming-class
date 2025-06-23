# import turtle
#
#
# screen = turtle.Screen()
# screen.title("Turtle Movement Control")
# screen.setup(600, 600)
#
# player = turtle.Turtle()
# player.shape('turtle')
# player.penup()
# player.speed(0)
#
# step = 20
# border = 280
#
#
# def go_up():
#     if player.ycor() + step <= border:
#         player.setheading(90)
#         player.forward(step)
#
#
# def go_down():
#     if player.ycor() - step >= -border:
#         player.setheading(270)
#         player.forward(step)
#
#
# def go_left():
#     if player.xcor() - step >= -border:
#         player.setheading(180)
#         player.forward(step)
#
#
# def go_right():
#     if player.xcor() + step <= border:
#         player.setheading(0)
#         player.forward(step)
#
# # when user press 'space' key, go to (0, 0)
# def reset_position():
#     player.goto(0, 0)
#
#
# trail_on = False
#
# def toggle_trail():
#     global trail_on
#     trail_on = not trail_on
#     if trail_on:
#         player.pendown()
#     else:
#         player.penup()
#
#
# colors = ["darkgreen", "red", "blue", "orange", "purple"]
# current_color = 0
#
# def change_color():
#     global color_index
#     color_index = (color_index + 1) % len(colors)
#     player.color(colors[color_index])
#
#
# # Listen to key presses
# screen.listen()
# screen.onkey(go_up, "Up")
# screen.onkey(go_down, "Down")
# screen.onkey(go_left, "Left")
# screen.onkey(go_right, "Right")
# screen.onkey(reset_position, 'space')
# screen.onkey(toggle_trail, 't')
# screen.onkey(change_color, 'c')
#
# turtle.mainloop()

# find min and max number from a given list
def find_min_max(numbers):
    min = numbers[0]
    max = numbers[0]

    for value in numbers:
        if value > max:
            max = value

        if value < min:
            min = value

    # return value to where the function being called, also exit from the function
    return min, max


print(find_min_max([1, 2, 4, -1, 5, 6]))




















