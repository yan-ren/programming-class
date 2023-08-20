# basic list methods
# a = [1, 2, 2]
# print(a)
#
# a[0] = 100
# print(a)
#
# a.append(100)
# print(a)
#
# a.insert(1, 300)
# a.insert(2, 1000)
# print(a)
#
# del a[0]
# print(a)
#
# a.remove(2)
# print(a)

# sum all numbers in the list
# a = [1, 2, 3, 4, 4, 4]
# n = 0
# sum = 0
#
# while n < len(a):
#     sum = sum + a[n]
#     n += 1
# print(sum / len(a))

# find the min value in the list
# a = [-1, -2, -2, -3]
# min = a[0]
# n = 0
# while n < len(a):
#     if min > a[n]:
#         min = a[n]
#     n += 1
#
# print(min)

# print each value in the list using while loop
a = [1, 2, 3, 4]
index = 0
while index < len(a):
    print(a[index])
    index += 1
