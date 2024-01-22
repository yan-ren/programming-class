s = 'abcdef'
s_reverse = ''

i = 0
while i < len(s):
    print(s[i])
    i += 1

for i in s:
    print(i)



i = len(s) - 1
while i >= 0:
    s_reverse += s[i]
    i -= 1


i = 0
while i < 10:
    if i == 2:
        i += 1
        continue
    print(i)
    i += 1




row = 1
while row <= 4:
    stars = 0
    while stars < row:
        print('*', end='')
        stars += 1
    print() # go to next line and ready for printing next row
    row += 1

print()
row = 1
while row <= 4:
    stars = 1
    while stars <= 4:
        print('*', end='')
        stars += 1
    print() # go to next line and ready for printing next row
    row += 1


def fizz_buzz(number):
    '''
    if number is divisible by 3 and 5, print fizzbuzz
    if number is divisible by 3 print fizz
    if number is divisible by 5 print buzz
    '''