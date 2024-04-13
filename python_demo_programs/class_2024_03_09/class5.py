# i = 0
# while i < 5:
#     print(i)
#     if i == 2:
#         continue
#     i += 1
#
# print('finish')

# i = 0
# while i < 5:
#     if i == 2:
#         i += 1
#         continue
#     print(i)
#     i += 1

# list1 = [1, 2, 3]
# list1.append(5)
# print(list1)
# list1.append('hello')
# print(list1)
# print(list1[2])
# print(list1[0])
# print(list1[4])
#
# del list1[3]
# print(list1)

# list = [-2, -1, -4, -5, -9]

# i = 0
# max_value = list[0]
# while i < len(list):
#     if list[i] > max_value:
#         max_value = list[i]
#     i = i + 1
#
# print(max_value)

# list = [1, 2, 4, 1, 2, 3, 1, 2, 3, 4]
# i = 0
# sum = 0
# while i < len(list):
#     sum = sum + list[i]
#     i += 1
#
# print(sum / len(list))

# import turtle
# import random
#
# wn = turtle.Screen()
# wn.setup(800, 600)
# t = turtle.Turtle()
# colors = ['yellow', 'red', 'green', 'purple']
# j = 0
# while j < 36:
#     # square
#     t.color(random.choice(colors))
#     i = 0
#     while i < 4:
#         t.forward(100)
#         t.left(90)
#         i += 1
#     j = j + 1
#     t.left(10)
#
# turtle.done()


# list = []
# while True:
#     value = input('enter a number: ')
#     if value == 'end':
#         break
#     else:
#         list.append(int(value))
#
# i = 0
# sum = 0
# while i < len(list):
#     sum = sum + list[i]
#     i += 1
#
# print(sum / len(list))

i = 0
while i < 4:
    j = 0
    while j < 4:
        print('*', end='')
        j += 1
    print()
    i += 1

'''
*
**
***
****
'''