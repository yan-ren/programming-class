# print(str(3) + '+')

instruction = input()
letters = ''
numbers = ''
turn = ''
for ch in instruction:
    if ch.isalpha():
        if turn != '':
            print(letters + ' ' + turn + ' ' + numbers)
            letters = ''
            turn = ''
            numbers = ''
        letters += ch
    elif ch.isdigit():
        numbers += ch
    elif ch == '+':
        turn = 'tighten'
    elif ch == '-':
        turn = 'loosen'

print(letters + ' ' + turn + ' ' + numbers)