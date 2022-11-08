'''
base case: when function stops calling itself
recursive case: how function calls itself
'''

'''
write a program to calculate the sum of a list
'''
def list_sum(nums):
    if len(nums) == 1:
        return nums[0]
    else:
        return nums[0] + list_sum(nums[1:])

'''
write a program to reverse a string
'''
'''
write a program to compute a^b in recursion
a^b = a*a^(b-1)
2^3 = 2*2^2
2^2 = 2*2^1
2^1 = 2*2^0
'''
def exp(a, b):
    if b == 0:
        return 1
    else:
        return a * exp(a, b-1)

'''
write a recursive function that calculates the nth fibonacci number
1, 1, 2, 3, 5, 8, ...
'''
'''
base case:


recursive case:
fib(n) = fib(n-1) + fib(n-2)
'''
def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n-1) + fib(n-2)

'''
Given a string, the task is to find whether it contains an additive sequence.

A string contains an additive sequence if its digits can make a sequence of numbers in which every number 
is addition of previous two numbers
e.g. s = "2,3,5,8,13"

'''

