N = int(input('Enter a value for N:'))
k = int(input('Enter a value for k:'))

i = 0
sum = 0
while i <= k: # create a while loop that runs k + 1 times
    sum += N * (10**i)
    i += 1

print('The shifty sum is', sum)

'''
sum = N * 10^0 + N * 10^1 + N * 10^2 + N * 10^3 + N * 10^4 ... + N * 10^k
'''