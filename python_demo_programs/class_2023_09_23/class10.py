s = 'Arthur'

# print(len(s))
# print(s[0])
# print(s[2])
# print(s[-5])
#
# print(s[0:3])

# print(s[0])
# print(s[1])
# print(s[2])
# print(s[3])
# print(s[4])
# print(s[5])
#
index = 0
while index < len(s):
    print(s[index])
    index += 1 # index = index + 1

# print reversely
# option 1, reverse the string
# s = s[::-1]
# index = 0
# while index < len(s):
#     print(s[index])
#     index += 1

index = len(s) - 1
while index >= 0:
    print(s[index])
    index = index - 1   # index -= 1


row = 1
while row < 5:
    col_stars = 0
    while col_stars < row:
        print('*', end='')
        col_stars += 1
    print()
    row += 1




