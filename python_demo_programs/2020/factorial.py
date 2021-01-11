
# use a loop to calculate n*(n-1)*(n-2)*(n-3)*...2*1,
# and return the result
def factorial(n):
    result = 1
    while n > 0:
        result = result * n
        n -= 1
    return result


print(factorial(5))
print(factorial(3))