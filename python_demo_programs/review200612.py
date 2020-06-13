# function = method = subroutine
# one feature: In large programs, we often need to do the same thing times.
# allow reusing a piece of code without duplicating it.

# def is the function symbol, followed by the function name, followed by the input parameters
def welcome_msg():
    print('welcome to the class')
    print('programming is not hard')

# name variable is an input
def welcome(name, address):
    print('welcome ' + name)
    print('you live in ' + address)


def calculation(a, b):
    sum = a + b
    diff = a - b
    return sum, diff


print('start')
welcome_msg()
welcome('steven', 'city a')
welcome('lu', 'city b')
welcome('jesse', 'city c')
res1, res2 = calculation(1, 2)
print(res1)
print(res2)
print('finish')

# practice: write a function takes three numbers, return the largest number
def compare(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# practice: write a function takes a list, return the sum of the list
# [1, 2, 3]
# 6
def sum_list(list):
    res = 0
    for i in list:
        res += i # res = res + i
    return res

# homework: write a function takes a list, return the average of the list
# [1, 2, 3]
# 2
