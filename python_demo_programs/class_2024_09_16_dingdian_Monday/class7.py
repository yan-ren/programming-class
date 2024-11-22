# '''
# 2018 j2
# '''
# input()
# yesterday = input()
# today = input()
# count = 0
#
# for index in range(len(yesterday)):
#     if today[index] == yesterday[index] and today[index] == 'c':
#         count += 1
#
# print(count)

N = int(input())
k = int(input())

# print(sum([N * 10 ** i for i in range(k+1)]))
res = N
for i in range(1, k+1):
    res = res + N * 10 ** i

print(res)
