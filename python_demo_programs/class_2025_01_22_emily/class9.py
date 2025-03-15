# L = [[2, 3], [4, 5]]
#
# # question: calculate the sum of all number from the list
# # solution1
# s = 0
# for numbers in L:
#     for num in numbers:
#         s += num
#
# print(s)
#
# # solution2
# s = 0
# for numbers in L:
#     s += sum(numbers) # sum is the built-in function from python
#
# print(s)
#
# # solution3
# i = 0
# s = 0
# while i < len(L):
#     j = 0
#     while j < len(L[i]):
#         s += L[i][j]
#         j += 1
#     i += 1
#
# print(s)

print(2 / 2.0)
print(2 / 2)
print(2 // 2)
print(2.0 // 2)

# / float division: give result as float
# // integer division: give result as integer
# 2 // 2.0 -> int -> float
# 2 // 2 -> int

# 3 // 2 -> int 1.5 -> 1
print(3 // 2)
# 3 // 2.0 -> int 1.5 -> 1 -> float -> 1.0
print(3 // 2.0)
print(3 / 2)

'''
Write a short program that prints each number from 1 to 100 on a new line. 

For each multiple of 3, print "Fizz" instead of the number. 

For each multiple of 5, print "Buzz" instead of the number. 

For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number.

e.g
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
...
14
FizzBuzz

1. understand the problem by look at the example or make examples
2. think about what are the major coding thing used in this question
    - loop/if
3. details
    - loop: from which number loop to which number
    - if: what's the condition for if else
'''

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)

# def tous_deux(liste):
#     for nombre in liste:
#         if nombre == 2:
#             return True
#         else:
#             return False

# print(tous_deux([2, 3, 3]))
'''
fix: write a function takes list of number, 
return True if only contains 2s
return False otherwise
'''

def tous_deux(liste):
    for nombre in liste:
        if nombre != 2:
            return False

    return True


print(tous_deux([1, 2, 2]))
print(tous_deux([2, 2, 2]))
print(tous_deux([2, 3, 3]))

# write a function take [2, 3, 3] return [True, False, False]
# def test(numbers):
#     res = []
#
#     for num in numbers:
#         if num % 2 == 0:
#             res.append(True)
#         else:
#             res.append(False)
#
#     return res
#
#
# print(test([2, 3, 3]))

# q1: given a list of numbers, write a function returns the number of
# positive value in the list
def count1(numbers):
    count = 0
    for num in numbers:
        if num > 0:
            count += 1

    return count
# q2: given a list of numbers, write a function returns the number of
# even value in the list
def count2(numbers):
    count = 0
    for num in numbers:
        if num % 2 == 0:
            count += 1

    return count

'''
Write a program to print multiplication table from 1 to 9
1x1=1
1x2=2
1x3=3
...
2x2=4
2x3=6

'''
# for first in range(1, 10):
#     for second in range(first, 10):
#         print(first, "x", second, '=', first*second)

import turtle

screen = turtle.Screen()
screen.setup(600, 800)

pen = turtle.Turtle()

for i in range(18):
    pen.circle(30)
    pen.left(20)

turtle.done()

'''
Exercise: Convert Kilometers to Miles
Write a program that asks the user for a distance in kilometers and displays the equivalent distance in miles.
(Formula: miles = km * 0.621371)

Exercise: Counting Consonants
Write a program that counts the number of consonants in a string provided by the user.

Exercise: Sum of Even Numbers
Write a program that calculates the sum of all even numbers from 1 to n, where n is a number given by the user.

Exercise: Factorial Calculation
Write a function factorial(n) that takes an integer n and returns its factorial.
'''