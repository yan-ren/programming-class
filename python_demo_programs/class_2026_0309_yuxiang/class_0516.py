# 1. read following programs and answer: how many times does print Hi
# i = 0
# while i < 8:
#     if i % 2 == 0 and i != 4:
#         print("Hi")
#     i += 1

# 2. What is the output?
# x = 10
# while x > 0:
#     if x % 3 == 0:
#         x -= 2
#     else:
#         x -= 1
# print(x)

# 3. How many lines of output?
for i in range(4):
    for j in range(i, 4):
        print(i, j)

'''
4. Which range() call produces the same values as [10, 7, 4, 1, -2]?
(a) range(10, -2, -3)   (b) range(10, -3, -3)   (c) range(10, -2, 3)   (d) range(10, 2, -3)
'''

'''
5. Which range() call produces [1, 4, 9, 16, 25]? (trick question)
(a) range(1, 26, 3)   (b) range(1, 6)**2   (c) None — you need a loop, not just range()   (d) range(1, 25)
'''
squares = []
for i in range(1, 6):
    squares.append(i**2)

s = "Programming"
print(s[0], s[-1], s[2:6], s[::-1][:3])

'''
Write a function count_digits(n) that returns the number of digits in a positive integer, using a while loop (no str()).
e.g.

count_digits(292) -> 13
'''
print(292 % 10)
print(292 // 10)

def count_digits(n):
    sum = 0

    while n > 0:
        last_digit = n % 10
        sum += last_digit
        n = n // 10

    return sum

print(count_digits(292))

'''
Write a function unique_letters(word) that takes a string and return the unique letters inside the string
'''

'''
Write fibonacci(n) two ways: (a) iterative with a for loop, (b) recursive.

Fibonacci sequence: a famous series of numbers where each number is the sum of the two preceding ones. 
Starting typically from 0 and 1, the sequence goes: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144... 

fibonacci(5) -> 3
'''
# def fib(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#
#     return fib(n - 1) + fib(n - 2)

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    a = 0
    b = 1
    for _ in range(n-1):
        c = a
        a = b
        b = a + c

    return b