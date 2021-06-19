# def print_number(n):
#     print(n)
#     # base case
#     if n == 0:
#         return
#     else:
#         print_number(n - 1)
#
#
# print_number(3)

# # write a factorial function using loop
# def factorial(n):
#     res = 1
#     while n > 0:
#         res = res * n
#         n -= 1
#     return res
#
# # factorial function recursive version
# def factorial(n):
#     if n == 1:
#         return n
#     else:
#         return n * factorial(n - 1)
#
# factorial(3)

# i = 0
# while i < 100:
#     print('hi')
#     i += 1

'''
write a non recursive function that calculate the factorial of n
'''
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


def factorial_recursive(n):
    if n == 1:
        return 1

    return n * factorial_recursive(n-1)

# a^b
# 2^3 = 2*2*2 = 
def power(a, b):
    result = 1
    for i in range(b):
        result = result * a
    return result
