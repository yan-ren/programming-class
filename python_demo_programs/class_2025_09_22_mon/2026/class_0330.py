# syntax == programming gramma
# print(2)
# print(3)
#
# i = 0
# while i < 10:
#     print(i)
#     i += 1
# print('finish')

# show multiplication table from 1x1 to 9x9, how to do it?
first = 1
while first <= 9:
    second = 1
    while second <= first:
        print(first, 'x', second, '=', first * second)
        second += 1
    first += 1

# draw a rectangle made of stars
# change width and height to see different shapes
height = 5
width = 8

row = 0
while row < height:
    col = 0
    line = ""
    while col < width:
        line = line + "* "
        col += 1
    print(line)
    row += 1

'''
exercise: use double loop, how to print following pattern
* 
* * 
* * * 
* * * * 
* * * * *
'''