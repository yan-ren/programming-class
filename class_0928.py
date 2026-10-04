
def pi_estimation_rec_private(i, precision):
    if i > precision:
        return 0

    return (-1) ** i / (2*i + 1) + pi_estimation_rec_private(i + 1, precision)


n = int(input('Enter a number:'))
if n <= 0:
    print('n must be a positive number')
elif n % 2 == 0 and n % 3 == 0:
    print('n is a multiple of 2 and 3')
elif n % 5 == 0:
    print('n is a multiple of 5')

'''
'4'* 5

'''