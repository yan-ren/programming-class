# d = {1: 'one', 'one': 1}
'''
immutable: unchangeable - int, boolean, float, string, tuple...
mutable: changeable - list, dictionary
'''
import math

# d = {[1, 2]: 'one'}
# print(d)

# l = []
# l.append(1)
# l[0] = 100
#
# t = 1, 2, 4, 1
# print(t[0])
# t[0] = 100
#
# for num in t:
#     print(num)

# t = 1,
# print(type(t))
# t = 1
# print(type(t))

# t = 1, 2, 3
# x, y = t
# print(t)

# N = int(input())
# k = int(input())
#
# # print(sum([N*(10**i) for i in range(k+1)]))
# '''
# 12 + 120 + 1200 + 12000
#
# 12*10^0 + 12*10^1 + 12*10^2 + 12*10^3
# '''
# sum = 0
#
# for i in range(k+1):
#     sum = sum + N * int(math.pow(10, i))
#
# print(sum)

row1 = input() # '16 3 2 13'
row1 = row1.split(' ') # ['16', '3', '2', '13']

row2 = input()
row2 = row2.split(' ')

row3 = input()
row3 = row3.split(' ')

row4 = input()
row4 = row4.split(' ')

row1_sum = 0
for num in row1:
    row1_sum += int(num)

row2_sum = 0
for num in row2:
    row2_sum += int(num)

row3_sum = 0
for num in row3:
    row3_sum += int(num)

row4_sum = 0
for num in row4:
    row4_sum += int(num)

col1_sum = int(row1[0]) + int(row2[0]) + int(row3[0]) + int(row4[0])
col2_sum = int(row1[1]) + int(row2[1]) + int(row3[1]) + int(row4[1])
col3_sum = int(row1[2]) + int(row2[2]) + int(row3[2]) + int(row4[2])
col4_sum = int(row1[3]) + int(row2[3]) + int(row3[3]) + int(row4[3])

