'''
2021 J3
'''
# direction = ''
#
# while True:
#     line = input()
#     if line == '99999':
#         break
#
#     two_digits = int(line[0:2])
#
#     if two_digits % 2 == 1:
#         direction = 'left'
#     elif two_digits % 2 == 0 and two_digits != 0:
#         direction = 'right'
#
#     print(direction, line[2:])

# s = 'abcdef'
# print(s[0])
# print(s[0:2])
N = int(input())
x = []
y = []
for i in range(N):
    line = input().split(',') # ['44', '62']
    x.append(int(line[0]))
    y.append(int(line[1]))
    