
# i = 0
# while i < 5:
#     print(i)
#     i = i + 1
#
# print(i)
# print('finish')

# start = int(input('Enter countdown duration:'))
# while start >= 0:
#     print(start)
#     start = start - 1

# is_valid = False
# while not is_valid:
#     age = input('Enter your age:')
#     if not age.isdecimal():
#         pass
#     else:
#         age = int(age)
#         if age >= 0.0 and age <= 150:
#             is_valid = True
#         # else:
#         #     is_valid = False

# i = 0
# while i < 2:
#     j = 0
#     while j < 2:
#         print(j)
#         j = j + 1
#     i = i + 1

# print(1, end='')
# print(2)

# size = int(input('Enter the size of square: '))
#
# row = 0
# while row < size:
#     col = 0
#     while col < size:
#         print('#', end='')
#         col += 1
#     # print('####')
#     print()
#     row += 1

i = 0
while i < 5:
    if i == 2:
        break
    print(i)
    i += 1

print('finish')