'''
stack
queue

recursion: a function calls itself
1. base case
2. recursive case
'''

def hello():
    print('Hello')
    hello()

# hello()

# def number(n):
#     if n == 0: # base case
#         return
#
#     print(n)
#     number(n-1) # recursive case
#
# number(4)

'''
factorial

n! = n * (n-1) * (n-2) ... * 1

n! = n * (n-1)!
(n-1)! = (n-1) * (n-2)!
...
2! = 2 * 1!
1! = 1

'''
# def factorial(n):
#     # use loop to calculate n! and return
#     result = 1
#     for i in range(1, n+1):
#         result = result * i
#
#     return result

# def factorial(n):
#     if n == 1:
#         return 1
#
#     return n * factorial(n-1)


'''
write a function that can calculate a^b 

a^b = a * a * ... * a


'''
# def power(a, b):
#     result = 1
#     for i in range(b):
#         result = result * a
#
#     return result
#
# print(power(2, 4))

def power(a, b):
    if b == 1:
        return a

    return a * power(a, b - 1)

'''
how to reverse a string using recursion
'abc' -> 'cba'
'''