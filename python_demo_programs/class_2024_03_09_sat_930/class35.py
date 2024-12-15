# 2020 j3
# N = int(input())
#
# x = []
# y = []
#
# # take all inputs
# for _ in range(N):
#     values = input().split(',')
#     x.append(int(values[0]))
#     y.append(int(values[1]))
#
# x_min = min(x)
# x_max = max(x)
# y_min = min(y)
# y_max = max(y)
#
# print(str(x_min - 1) + "," + str(y_min - 1))
# print(str(x_max + 1) + "," + str(y_max + 1))

# d = {}
# s = 'baaabccdef'
#
# for ch in s:
#     if ch in d:
#         d[ch] = d[ch] + 1
#     else:
#         d[ch] = 1
#
# print(d)
#
# # loop dictionary by key
# for k in d.keys():
#     print(k, d[k])
#
# for k, v in d.items():
#     print(k, v)

s = '+++===!!!!'

index = 0
count = 1

while index < len(s) - 1:
    if s[index] == s[index + 1]:
        count += 1
    else:
        print(count, s[index])
        count = 1

    index += 1

print(count, s[index])