# x = 2 # assign value 2 to variable x
# y = 3
#
# print(x == y)
# print(x != y)
# print(x > y)
# print(x >= y)
# print(x < y)
# print(x <= y)

# boolean used together with other things, e.g. if elif, looping

# if x + y > 0 and x - y > 0:

# x = int(input('Enter the first value'))
# y = int(input('Enter the second value'))

# if x > y:
#     print('x is bigger')
# elif x < y: # optional, use it if need more condition
#     print('y is bigger')
# else: # else is optional, use it depends on logic
#     print('x and y is the same')

# x = int(input('Enter a number'))
#
# if x > 100: # narrow condition on top
#     print('x is bigger than 100')
# elif x > 10: # wilder condition on bottom
#     print('x is bigger than 10')
# elif x > 0:
#     print('x is bigger than zero')
# else:
#     print('whatever')

# nested if statement
# x = 1
#
# if x > 0:
#     if x % 2 == 0:
#         print('positive even')
# else:
#     print('negative')

# x = int(input('Enter first value:'))
# y = int(input('Enter second value:'))
# z = int(input('Enter third value:'))
#
# if x > y and x > z:
#     print('x is the largest')
# elif y > x and y > z:
#     print('y is the largest')
# else:
#     print('z is the largest')
#
# if x > y:
#     if x > z:
#         print('x is the biggest')
#     else:
#         print('z is the biggest')
# else:
#     if y > z:
#         print('y is the biggest')
#     else:
#         print('z is the biggest')

# looping in python: for and while
i = 0
while i < 10: # loop header
    print(i) # loop body
    i = i + 1
#
# print('last line: ', i)

# i = 10
#
# while i >= 0:
#     print(i)
#     i = i - 1

# infinite loop
# while True:
#     print('Hello')
#
# print('done')

# 0, 1, 2, 3, 4, 5, ... 9
for num in range(10):
    if num == 3:
        break

    if num == 4:
        break
    print(num)

for c in 'abc':
    print(c)

