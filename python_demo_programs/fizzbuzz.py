# version1
n = 1

while n <= 50:
    if n % 3 == 0 and n % 5 == 0:
        print('fizzbuzz')
    elif n % 3 == 0:
        print('fizz')
    elif n % 5 == 0:
        print('buzz')
    else:
        print(n)
    n += 1

# version2
n = 1

while n <= 50:
    divide3 = n % 3 == 0
    divide5 = n % 5 == 0

    if divide3 and divide5:
        print('fizzbuzz')
    elif divide3:
        print('fizz')
    elif divide5:
        print('buzz')
    else:
        print(n)
    n += 1