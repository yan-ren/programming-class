# l = []
#
# # method 1
# for i in range(100):
#     l.append(0)
#
# # method 2
# l = [0 for i in range(100)]
#
# # method 3
# l = [0] * 100
# print(l)

# ['apple', 'orange', 'pear'] -> [['apple', 5], ['orange', 6], ['pear', 4]]
# list = ['apple', 'orange', 'pear']
# new_list = [[fruit, len(fruit)] for fruit in list]
#
# list = [1, 2, 3, 4]
# new_list = ['even' if num % 2 == 0 else 'odd' for num in list]

# s = 'hello'
# res = s.split()
# # res = list(s)
# print(res)

# s = 'a'
# print(s * 10)

# print(1, end='')
# print(2)
# print()

# 2019 j2
# L = int(input())
#
# for _ in range(L):
#     text = input() # '9 A'
#     items = text.split(' ')
#     # print(items[1] * int(items[0]))
#     for i in range(int(items[0])):
#         print(items[1], end='')
#     print()

# 2018 j2
input()
yesterday = input().lower()
today = input().lower()
count = 0

for i in range(len(yesterday)):
    if yesterday[i] == 'c' and today[i] == 'c':
        count += 1

print(count)