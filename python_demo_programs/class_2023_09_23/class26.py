'''
write non-recursive function for palindrome checking
and
write recursive function for palindrome checking
'''

# s = input('enter a string for palindrome checking:')

# def is_palindrome_nonrecursion(s):
#     index = 0
#     while index < len(s) / 2:
#         if s[index] != s[len(s) - 1 - index]:
#             return False
#         index += 1
#
#     return True
#
# def is_palindrome(s):
#     if len(s) <= 1:
#         return True
#
#     # recursive case
#     if s[0] == s[len(s) - 1]:
#         return is_palindrome(s[1 : len(s) - 1])
#     else:
#         return False

# def summation(n):
#     if n == 1:
#         return 1
#
#     return n + summation(n-1)

'''
write recursive function that reverse a string
input: 'abcdef'
return: 'fedcba'
'''
# def reverse(s):
#     if len(s) == 1:
#         return s
#
#     return s[len(s) - 1] + reverse(s[0:len(s) - 1])

'''
rewrite the binary search using recursion
'''
numbers = [1, 3, 4, 5, 6, 7, 10]
target = 3
# def binary_search(numbers, target):
#     left = 0
#     right = len(numbers) - 1
#
#     while left <= right:
#         mid = (left + right) // 2
#         # check if target is at mid
#         if numbers[mid] == target:
#             return True
#         elif numbers[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#
#     return False

# def binary_search(numbers, target, left, right):
#     if left > right: # base case: target not found in list
#         return -1
#     mid = (left + right) // 2
#     if numbers[mid] == target:
#         return mid
#     # if target is smaller that mid, continue binary search on the left side
#     if numbers[mid] > target:
#         return binary_search(numbers, target, left, mid - 1)
#     else:
#         return binary_search(numbers, target, mid + 1, right)

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fib(n - 1) + fib(n-2)