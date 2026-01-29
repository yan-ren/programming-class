'''
2022 J3
'''
instruction = input() # 'AFB+8HC-4'
letter = ''
sign = ''
number = ''
for ch in instruction:
    if ch.isalpha():
        if sign != '':
            print(letter, sign, number)
            letter = ''
            sign = ''
            number = ''
        letter += ch
    elif ch.isdigit():
        number += ch
    elif ch == '+':
        sign = 'tighten'
    elif ch == '-':
        sign = 'loosen'

print(letter, sign, number)