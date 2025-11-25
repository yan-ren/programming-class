'''
control flow
- conditional: if elif else
- loop:
    - while loop
    - for loop
'''
i = 0
while i < 10: # loop header
    print('Hello')
    i = i + 1

# print(i)

# n = 1
# sum = 0
# while n <= 100:
#     sum = sum + n
#     n += 1

n = 2
while n <= 100:
    print(n)
    n += 2

n = 1
while n <= 100:
    if n % 2 == 0:
        print(n)
    n += 1

'''
homework:

count down program:

use python turtle to write a count down. Ask user for a number, from that number, count down to 0
'''
import turtle

wn = turtle.Screen()
wn.setup(600, 600)
