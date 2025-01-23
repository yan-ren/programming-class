'''
line = input()

instruction = ''
operation = ''
turn = ''

for i in range(len(line)):
    if line[i].isalpha():
        if operation != '' and turn != '':
            print(instruction, operation, turn)
            instruction = ''
            operation = ''
            turn = ''
        instruction += line[i]
    elif line[i].isdigit():
        turn += line[i]
    elif line[i] == '+':
        operation = 'tighten'
    elif line[i] == '-':
        operation = 'loosen'


print(instruction, operation, turn)
'''

