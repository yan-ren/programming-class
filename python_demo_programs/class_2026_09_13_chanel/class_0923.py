# a = 5
# b = 3
#
# print(a / b)
# print(a // b) # integer division
#
# print(a % b)
#
# print(7 % 6)
#
# print(5 % 5)
# print(2 % 4) # module
#
# print(0 % 2)

# n = int(input('Enter a number: '))
#
# while n >= 1:
#     if n % 2 == 0:
#         print(n // 2)
#         n = n // 2
#     elif n % 2 == 1: # odd
#         print(3 * n + 1)
#         n = 3 * n + 1
#     else:
#         print(n)

# number = float(input('Enter a real number: '))
# sum = 0
# count = 0
# sum_squared = 0
#
# while number != 0:
#     sum += number
#     count += 1
#     sum_squared += number**2
#     number = float(input('Enter a real number: '))
#
# print('Average:', round(sum / count, 2))
# print('Sum squared:', round(sum_squared, 2))

a = int(input())
b = int(input())

j = a
while j <= b:
    count = 0
    i = 1
    while i <= a:
        if a % i == 0:
            count += 1
        i += 1

    if count == 4:
        print(j)

    j += 1