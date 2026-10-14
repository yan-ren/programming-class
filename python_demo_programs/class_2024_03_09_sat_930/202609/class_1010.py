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

