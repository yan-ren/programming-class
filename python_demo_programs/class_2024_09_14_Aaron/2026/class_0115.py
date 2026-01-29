'''
2019 CCC J3
'''

# '+++===!!!!'

# N = int(input())

def code(text):
    current = ''
    count = 0
    result = []

    for ch in text:
        if ch != current and current != '':
            result.append(str(count))
            result.append(current)
            count = 1
        else:
            count += 1

        current = ch

    result.append(str(count))
    result.append(current)
    return ' '.join(result)

print(code('+++===!!!!'))