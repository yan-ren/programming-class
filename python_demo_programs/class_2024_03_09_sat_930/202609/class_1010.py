'''
recursion: a function calls itself

basic case
recursive case
'''

# def message():
#     print('hello')
#     message()
#
#
# message()

'''
example 1: write a function that calculates the a^b, don't use a**b
'''
# def power(a, b):
#     result = 1
#     for i in range(b):
#         result *= a
#
#     return result
#
# print(power(2, 3))

def power(a, b):
    if b == 1:
        return a

    return a * power(a, b - 1)

'''
example 2: write a function that calculate the factorial of a
5! = 5 * 4 * 3 * 2 * 1
'''
# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#
#     return result

# def factorial(n):
#     if n == 1:
#         return 1
#
#     return n * factorial(n-1)

'''
example 3: write a function that calculates the nth fibonacci number
'''