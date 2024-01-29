# recursive approach
# base case, recursive case
'''
def fib(n):
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib(n-1) + fib(n-2)
    return result
'''

'''
mem = {}

def fib(n):
    if n in mem:
        return mem[n]

    if n == 1 or n == 2:
        result = 1
    else:
        result = fib(n-1) + fib(n-2)

    mem[n] = result
    return result
'''
'''
def fib(n):
    if n == 1 or n == 2:
        return 1

    bottom_up = [0] * n
    bottom_up[0] = 1
    bottom_up[1] = 1

    index = 2
    while index < n:
        bottom_up[index] = bottom_up[index-1] + bottom_up[index-2]
        index += 1

    return bottom_up[n-1]
'''
