# N = int(input())
#
# days = [0] * 5
#
# for _ in range(N):
#     people = input() # '..Y.Y'
#     day = 0
#     while day < len(people):
#         if people[day] == 'Y':
#             days[day] += 1
#         day += 1
#
# max_people = max(days)
# result = []
#
# day = 0
# while day < len(days):
#     if days[day] == max_people:
#         result.append(day + 1)
#     day += 1
#
# print(*result, sep=',')

s = 'AFB+88HC-444' # '+88HC-444'


print(s[3:])
print(s)
s = s[3:]
print(s)