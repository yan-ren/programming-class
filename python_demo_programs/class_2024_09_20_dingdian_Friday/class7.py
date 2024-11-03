# import random
#
#
# target = random.randint(0, 20)
#
# running = True
# chances = 3
#
# while running:
#     if chances == 0:
#         print('Game Over')
#         running = False
#     else:
#         guess = int(input('Guess a number between 0 to 20:'))
#         if guess > target:
#             print('Too high')
#         elif guess < target:
#             print('Too low')
#         else:
#             print('Correct')
#             running = False
#         chances -= 1
#
# # how to add chances

# print(2, end='')
# print()
# print(3)

# row = 0
# while row < 4:
#     col = 0
#     while col < row + 1:
#         print('#', end='')
#         col += 1
#     print()
#     row += 1

'''
homework:

####
###
##
#
'''

# more example about using while loop with turtle
# import turtle
#
#
# screen = turtle.Screen()
# screen.setup(600, 800)
# t = turtle.Turtle()
#
# # distance = 5
# # angle = 45
# # while distance < 200:
# #     t.forward(distance)
# #     t.right(angle)
# #     distance += 2
#
# screen.bgcolor('black')
# t.color('yellow')
#
# length = 100
# angle = 144
# count = 0
#
# while count < 10:
#     for _ in range(5):
#         t.forward(length)
#         t.right(angle)
#     t.penup()
#     t.forward(10)
#     t.pendown()
#     count += 1
#
# turtle.done()

# i = 0
# while i < 10:
#     j = 0
#     while j < 4:
#         if j == 4:
#             break
#         print(j)
#         j += 1
#     i += 1
#
# print(i)

while True:
    user_input = input('Enter a word or type exit to quit')
    if user_input == 'exit':
        break

    print('You entered', user_input)



















