'''
https://github.com/loucadufault/420-LCU-05/blob/master/Assignment-1/A-1_instructions.pdf
'''

running = True
low = 1
high = 100

print('Please think of a number between 1 and 100.')
while running:
    guess = (low + high) // 2
    print('Is your secret number', guess)
    answer = input('Enter h if my guess is too high, l if too low, or c if am correct: ')
    if answer == 'h':
        high = guess


