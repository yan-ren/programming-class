# s = '44,62'
# # print(s.split(','))
# items = s.split(',')
# print(int(items[0]), int(items[1]))
'''
2020 J3
'''

# N = int(input())
# x = []
# y = []
#
# for _ in range(N):
#     line = input().split(',')
#     x.append(int(line[0]))
#     y.append(int(line[1]))
#
# print(min(x) - 1, min(y) - 1, sep=',')
# print(max(x) + 1, max(y) + 1, sep=',')

'''
2019 J3
'''
N = int(input())

for _ in range(N):
    line = input()
    cur = line[0]
    count = 1

    for index in range(1, len(line)):
        if line[index] == cur:
            count += 1
        else:
            print(count, cur)
            cur = line[index]
            count = 1

