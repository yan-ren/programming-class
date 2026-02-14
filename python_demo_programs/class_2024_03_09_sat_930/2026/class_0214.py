# K = int(input())
# m = int(input())
#
# friends = [0] * (K+1)
# # print(friends)
# for i in range(1, len(friends)):
#     friends[i] = i
#
# # print(friends)
#
# for _ in range(m):
#     r = int(input())
#     new_list = [0]
#     for i in range(1, len(friends)):
#         if i % r != 0:
#             new_list.append(friends[i])
#     friends = new_list
#
# for i in range(1, len(friends)):
#     print(friends[i])

T = int(input())
C = int(input())

chores = []
for _ in range(C):
    chores.append(int(input()))

chores.sort()

total_time = 0
count = 0
for time in chores:
    if total_time + time <= T:
        total_time += time
        count += 1
    else:
        break

print(count)