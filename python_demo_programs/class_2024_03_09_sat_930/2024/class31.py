# antonia = 100
# david = 100
#
# round = int(input())
#
# for _ in range(round):
#     # current = list(map(int, input().split(' ')))
#     # map(int, ['5', '6']) -> list(map([5, 6])) -> [5, 6]
#     # current = input().split(' ') # ['5', '6']
#     # ['5', '6'] -> [5, 6]
#     current = list(map(int, input().split(' ')))
#
#     if current[0] > current[1]:
#         david -= current[0]
#     elif current[1] > current[0]:
#         antonia -= current[1]
#
#
# print(antonia)
# print(david)


# unpacking
# l = [1, 2]
# a, b = l

# word = input()
# target = 'IOSHZXN'
#
# # count = 0
# sign = True
#
# for letter in word:
#     if letter not in target:
#         sign = False
#
# if sign:
#     print('YES')
# else:
#     print('NO')

s = 'abcdef'
print(s.count('d'))
print(s.index('d'))
print(s.startswith('abc'))
print(s.endswith('fd'))
print(len(s) - 1)
print(s.isalpha()) # return true if all character in string are in the alphabet
print(s.isdigit()) # return true if all characters in the string are digits


l = [10, 12, 3, 4]
print(len(l) - 1)
print(l.count(2))

l.sort(reverse=True) # l is changed to sorting order

l_s = sorted(l, reverse=True) # l is not changed but return a new sorted list
print(l)
print(l_s)

'''
2024 j3
'''