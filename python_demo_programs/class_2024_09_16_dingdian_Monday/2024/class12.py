'''
CCC 2021 J3
'''

# s = '57234'
# s[0]
# s[1]
# s[2:] # slicing
pre = ''

while True:
    value = input()
    if value == '99999':  
        break

    # todo
    sum = int(value[0]) + int(value[1])
    direction = ''
    if sum == 0:
        direction = pre
    elif sum % 2 == 1:
        direction = 'left'
    else:
        direction = 'right'

    print(direction, value[2:])
    pre = direction

'''
2020 J3
'''