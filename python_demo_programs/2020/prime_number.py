# write a python program to check if a number is prime or not

number = int(input('enter a number:'))
n = 1
counter = 0
while n <= number:
    if number % n == 0:
        counter += 1
    n += 1

if counter > 2:
    print('not prime number')
else:
    print('prime number')