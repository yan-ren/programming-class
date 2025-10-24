'''
how to reverse a string using recursion
'abc' -> 'cba'
'''
# def reverse_non_recursion(s):
#     new_s = ''
#
#     for ch in s:
#         new_s = ch + new_s
#
#     return new_s
#
# print(reverse_non_recursion('abc'))
#
# def reverse(s):
#     if len(s) == 1:
#         return s
#     return reverse(s[1:]) + s[0]

'''
fibonacci sequence


'''
# def fib(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#
#     return fib(n-1) + fib(n-2)
#
# def fib_non_recursion(n):
#     first = 0
#     second = 1
#     third = 0
#
#     if n == 0 or n == 1:
#         return n
#
#     for i in range(n-2):
#         third = first + second
#         first = second
#         second = third
#
#     return third

# palindrome
def is_palindrome(s):
    if len(s) <= 1:
        return True

    if s[0] != s[-1]:
        return False

    return is_palindrome(s[1:-1])