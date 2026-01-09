# s = 'abcde'
# l = ['a', 'b', 'c', 'd', 'e']
#
# # convert s to l, using list()
# print(list(s))
#
# # convert l to s
# print(':'.join(l))
#
# n = ['1', '2', '3', '1', '2']
# print(''.join(n))

line = input()

index = 0

letters = ''
numbers = ''
sign = ''

while index < len(line):
    if line[index].isalpha():
        if sign != '':
            print(letters, sign, numbers)
            letters = ''
            sign = ''
            numbers = ''
        letters += line[index]
    elif line[index] == '+':
        sign = 'tighten'
    elif line[index] == '-':
        sign = 'loosen'
    elif line[index].isdigit():
        numbers += line[index]

    index += 1

print(letters, sign, numbers)
