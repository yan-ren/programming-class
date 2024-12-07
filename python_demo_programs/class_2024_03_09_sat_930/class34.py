# s = '1'
#
# print(s.isdigit())
# # print(s == '+')
# print(s in '0123456789')

previous_dir = ''
while True:
    value = input()
    if value == '99999':
        break

    direction = ''
    sum = int(value[0]) + int(value[1])
    if sum == 0:
        direction = previous_dir
    elif sum % 2 == 0:
        direction = 'right'
    else:
        direction = 'left'

    print(direction, value[2:])
    previous_dir = direction

# 2020 j3