import turtle
import math


# wn = turtle.Screen()
# t = turtle.Turtle()
#
# for i in range(4):
#     t.forward(100)
#     t.left(90)
#
#
# wn.exitonclick()

# else:
#     print('no money receive')

'''
for
while
'''

# i = 0
# while i < 10:
#     print(i)
#     i += 1

# print(i)

'''
list
'''
l = [1, 2, 3, 4]
print(l[0])
print(l[1])

for i in l:
    print(i)


index = 0
while index < len(l):
    print(l[index])
    index += 1 # index = index + 1

l = [1, 2, 3, 3, 3, 3]

d = {'a': 1, 'b': 1}
print(d['a'])

def welcome():
    print('hello')
    print('welcome to the class')


def addition(a, b):
    return a + b


welcome()
welcome()
print(addition(1, 2))


print(range(10)) # from 0 to 9
print(range(1, 10)) # from 1 to 9

for r in range(1, 6):
    for c in range(r):
        print('*', end=' ')
    print()