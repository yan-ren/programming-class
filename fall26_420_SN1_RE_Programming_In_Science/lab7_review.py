import matplotlib.pyplot as plt
from math import sin, pi

# N = 10
# x = [0] * N
# y = [0] * N
# i = 0
#
# while i < N:
#     x[i] = 2 * pi * i / N # 2pi / 10 * i
#     y[i] = sin(x[i]) # x[i] ** 2 -> y = x^2
#     i += 1

# x = [0, 1, 2, 3, 4, 5]
# y = [0, 1, 2, 3, 4, 5]
# print(x)
# print(y)
# plt.plot(x, y, color = 'red')
# plt.show()

from random import randint, seed
n = int(input("Enter the desired list length: "))
seed(n) # Initialize the random number generator.
# Generate a list of n numbers between -100 and +100, inclusive.
ls = [0] * n
i = 0
while i < n:
    ls[i] = randint(-100, 100)
    i += 1

print(ls)

i = 0
s = 0
while i < len(ls):
    s += ls[i]
    i += 1

print(s)

print(sum(ls))
print(max(ls))
print(min(ls))
# [59, -35, 89, -9, 76]