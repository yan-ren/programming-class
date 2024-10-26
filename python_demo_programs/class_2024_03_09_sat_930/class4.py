# sum = 0
#
# counter = 0
# run = True
#
# while run:
#     number = input('enter a number:')
#     if number == 'end':
#         run = False
#     else:
#         sum = sum + int(number)
#         counter = counter + 1
#
# print(sum / counter)

# i = 0
# while i < 3:
#     j = i
#     while j < 3:
#         print(j)
#         j = j + 1
#     i = i + 1

# import turtle
#
#
# wn = turtle.Screen()
# wn.setup(800, 600)
# t = turtle.Turtle()
# t.shape('turtle')
# t.hideturtle()
# # t.penup()
# t.forward(100)

# j = 0
# while j < 36:
#     # square
#     t.color('yellow')
#     i = 0
#     while i < 4:
#         t.forward(100)
#         t.left(90)
#         i += 1
#     # triangle
#     t.color('red')
#     i = 0
#     while i < 3:
#         t.forward(50)
#         t.left(120)
#         i += 1
#
#     j = j + 1
#     t.left(10)

# turtle.done()

# i = 0
# while i < 5:
#     print(i)
#     if i == 2:
#         break
#     i += 1
#

i = 0
while i < 5:
    print(i)
    if i == 2:
        continue
    i += 1

print('finish')