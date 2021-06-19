# write a non-recursive function that return n!
def factorial(n):
    result = 1
    while n >= 1:
        result *= n
        n -= 1
    return result


def factorial_recursive(n):
    # base case
    if n == 1:
        return 1

    return n * factorial_recursive(n-1)

print(factorial_recursive(1))

"""
Given a string s consists of some words separated by spaces, 
return the length of the last word in the string. If the last word does not exist, return 0.

example:
s = "Hello World"
length = 5

s = "good morning Tom"
length = 3

s = "welcome"
length = 6
"""

s = "Hello World"
l = s.split(" ")
print(len(l[len(l) - 1]))

# return a^b, non recursive
def power(a, b):
    result = 1
    while b > 0:
        result = result * a
        b -= 1

    return result

print(power(2, 3))

# given a string, how to print string in reversed order
def reverse_print(str):
    if len(str) == 1:
        print(str)
        return
    reverse_print(str[1:])
    print(str[0])

# write a recursive function that calculate n + (n-1) + (n-2) ... + 1

'''
given a list of number, write a recursive function to sum all elements in the list
'''