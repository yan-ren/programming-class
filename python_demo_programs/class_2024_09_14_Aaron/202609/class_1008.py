'''
recursion: a function calls itself
'''

# def msg():
#     print('msg')
#     msg()
#
# msg()

# def count(n):
#     print(n)
#     if n == 1:
#         return
#
#     count(n-1)
#
# count(10)

'''
example 1: power
write a function that calculate a^b
e.g.
a = 2
b = 3
result = 8
'''
# non-recursion
# def power(a, b):
#     res = 1
#     for i in range(b):
#         res *= a
#
#     return res

# recursion
# def power(a, b):
#     if b == 1:
#         return a
#
#     return a * power(a, b - 1)

'''
example 2
write a function that calculate fibonacci sequence of n
e.g.
n = 5
result = 3
'''
# non-recursion
def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1

    first = 0
    second = 1
    third = 0

    for i in range(2, n):
        third = first + second
        first = second
        second = third

    return third

print(fibonacci(5))

# recursion
def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)