# print(2, end='')
# print(3)
# print()
# print(4)

# for i in range(4):
#     for j in range(4):
#         print('*', end='')
#     print()

i = 0
while i < 4:
    j = 0
    while j < 4:
        print("*", end='')
        j += 1
    i += 1
    print()