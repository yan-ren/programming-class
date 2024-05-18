'''
recursion: function calls itself
'''

# def method():
#     print("method")
#     method()
#
# method()

'''
factorial, 5! = 5*4*3*2*1
write a function that calculate the n!
'''
def factorial_nonrecursion(n):
    res = 1
    # range(1, n+1) -> 1, 2, ..., n
    for value in range(1, n+1):
        res = res * value

    return res


print(factorial_nonrecursion(4))

def factorial(n):
    # base case
    if n == 1:
        return 1

    return n * factorial(n-1)

print(factorial(4))

'''
write a function that calculate a^b
'''
def power_nonrecursion(a, b):
    res = 1
    for _ in range(b):
        # res = res * a
        res *= a
    return res


def power(a, b):
    if b == 0:
        return 1

    return a * power(a, b - 1)

'''
write non-recursive function for palindrome checking
and 
write recursive function for palindrome checking
'''

s = "abbc"
print(s[1:len(s)-1])