# instruction = input()
#
# letters = ''
# sign = ''
# digits = ''
#
# for ch in instruction:
#     # if ch.isalpha()
#     if 'A' <= ch <= 'Z':
#         if sign != '' and digits != '':
#             print(letters, sign, digits)
#             letters = ''
#             sign = ''
#             digits = ''
#
#         letters += ch
#     elif ch.isdigit():
#         digits += ch
#     elif ch == '-':
#         sign = 'loosen'
#     elif ch == '+':
#         sign = 'tighten'
#
# print(letters, sign, digits)

'''
2021 J3
'''
previous = ''
while True:
    line = input()
    if line == '99999':
        break

    direction = ''
    sum = int(line[0]) + int(line[1])
    if sum % 2 == 1:
        direction = 'left'
    elif sum % 2 == 0 and sum != 0:
        direction = 'right'
    elif sum == 0:
        direction = previous

    previous = direction

    print(direction, line[2:])

