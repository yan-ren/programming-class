'''
write a function that reverse a string

"abc" -> "cba"

reverse("abc") -> "c" + reverse("ab")
reverse("ab") -> "b" + reverse("a")
reverse("a") -> return "a"

base case: if string only has one character, just return string
recursive case:
'''
# def reverse(str):
#     if len(str) == 1:
#         return str
#     else:
#         return str[len(str)-1] + reverse(str[:len(str)-1])
#
#
# print(reverse("abc"))

'''
Fibonacci sequence

write a non-recursive function that calculates the nth fibonacci number
'''
def fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fib(n-1) + fib(n-2)

'''
Write a Python program of recursion list sum
e.g. [1, 2, [3,4], [5,[6,7]]
return 21

base case: when element is single value, just add to the sum
recursive case: when element is a list, call function get the sum of the list
'''
def recursive_sum(l):
    res = 0
    for item in l:
        if isinstance(item, int):
            res += item
        else:
            res = res + recursive_sum(item)
    return res
