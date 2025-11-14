# dusa = int(input())
#
# while True:
#     yobis = int(input())
#
#     if dusa > yobis:
#         dusa += yobis
#     else:
#         break
#
# print(dusa)

# d = {
#     'a': 1
# }
#
# pepper = 'a'
# print(d[pepper])

# n = int(input())
# star = 0
#
# for _ in range(n):
#     score = int(input())
#     foul = int(input())
#
#     rating = 5 * score - 3 * foul
#     if rating > 40:
#         star += 1
#
# if n == star:
#     print(str(star) + "+")
# else:
#     print(star)

total = int(input())
current = int(input())
infected = int(input())

day = 0
today = current
while current <= total:
    today = today * 5
    current = today + current
    day += 1

print(day)