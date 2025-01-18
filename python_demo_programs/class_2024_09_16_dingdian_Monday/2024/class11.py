'''
2022 Problem J3: Harp Tuning
'''
line = input()
instruction = ''
operation = ''
turn = ''

for i in range(len(line)):
    if line[i].isalpha():
        if operation != '' and turn != 0:
            if operation == '+':
                print(instruction, 'tighten', turn)
            else:
                print(instruction, 'loosen', turn)
            instruction = ''
            operation = ''
            turn = ''
        instruction += line[i]
    elif line[i].isdigit():
        turn += line[i]
    elif line[i] == '+' or line[i] == '-':
        operation = line[i]

if operation == '+':
    print(instruction, 'tighten', turn)
else:
    print(instruction, 'loosen', turn)
