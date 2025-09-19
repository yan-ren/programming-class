'''
1. Print All Numbers from 50 to 60
2. Count Down by Twos from 20 to 0, e.g. 20 18 16 ... 0
3. Double Until Over 1000
Start with 1. Keep doubling it (multiply by 2) until the value is over 1000. Print all the values.
1 2 4 8 16 ...
'''
# count = 20
# while count >= 0:
#     print(count)
#     count -= 2
#
#
# i = 1
# while i < 1000:
#     print(i)
#     # i = i * 2
#     i *= 2

# j = 1
# while j <= 5:
#     i = 1
#     while i <= 5:
#         print(i)
#         i += 1
#     j += 1

# print(1, end='')
# print(2)

# j = 1
# while j < 5:
#     i = 1
#     while i < 5:
#         print('*', end = '')
#         i += 1
#     j += 1
#     print()

'''
*
**
***
****
'''
# j = 1
# while j < 5:
#     i = 1
#     while i <= j:
#         print('*', end = '')
#         i += 1
#     j += 1
#     print()
'''
1 x 1 = 1
2 x 1 = 2
2 x 2
3 x 1
3 x 2
3 x 3
4 x 1
4 x 2
4 x 3
4 x 4
'''

# first = 1
# while first <= 9:
#     second = 1
#     while second <= first:
#         print(first, 'x', second, '=', first * second)
#         second += 1
#     first += 1


'''
1 1 1
2 2 2
3 3 3
4 4 4
5 5 5
'''
# print(1, end=' ')


import turtle

wn = turtle.Screen()
wn.setup(800, 800)

pen = turtle.Turtle()

j = 0
length = 100
while j < 10:
    i = 0
    while i < 4:
        pen.forward(length)
        pen.left(90)
        i += 1
    length += 10
    j += 1
turtle.done()

'''
1 2 3
4 5 6
7 8 9
'''