# exercise: write a recursive function that prints from 1 to 10

# def count(n):
#     if n > 10:
#         return
#     print(n)
#     count(n+1)
#
# count(1)

# how to calculate 1+2+3+...+n using recursion
def sum(n):
    if n == 1000:
        return 1000

    return n + sum(n-1)

print(sum(2000))

'''
1. Write a for loop that displays the following set of numbers:
0 10 20 30 40 50 60 70 80 90 100
'''
i = 0
while i <= 100:
    print(i, end=' ')
    i += 10
