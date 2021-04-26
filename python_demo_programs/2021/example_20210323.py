# def method2():
#     x = 20
#
#
# def method1():
#     method2()
#     x = 2
#
#
# x = 1 # start the program at global scope, x is defined on the global scope
# x = 100 # still on global scope, find x, update its value
# method1()
'''
reverse integer
Given an integer x, return the x with its digits reversed

example
input: 123
output: 321

input: -123
output: -321
'''
# [1, 2, 3, 4] -> [4, 3, 2, 1] -> 4321
# def reverseInteger(x):
#     reverse = str(x)[::-1]
#     return int(reverse)
def reverseInteger(x):
    res = 0

    while x != 0:
        digit = x % 10          # get the right most digit
        res = res * 10 + digit  # * 10 shifts all digits in res to left by one place
        x = x // 10             # remove the right most digit

    return res


print(reverseInteger(12345))
'''
digit = 4 -> 4 * 10 -> 4 0
res = 54
'''