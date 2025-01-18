# word = 'ABe'
#
# print([ch for ch in word.lower() if ch not in 'aeiou'])
#
# # [0, 1, 2, 3] -> [1, 3, 5, 7]
# l = [0, 1, 2, 3]
# print([num * 2 + 1 for num in l])

# l = [3, 8, 9, 5]
#
# print(7/2)
# print(7//2)
# print(7%2)
#
# print([True if num % 3 else False for num in l])
# print([num % 3 == 0 for num in l])

# words = ['apple', 'orange', 'pear']
# # print(words[2])
#
# print([word.upper()[0] for word in words])

# 2020 J2
P = int(input())
N = int(input())
R = int(input())

total = N
day = 0
while total <= P:
    N = N * R
    total = total + N
    day += 1

print(day)