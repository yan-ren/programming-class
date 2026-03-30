'''
given a list of numbers, find the largest prime number
'''
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def find_largest_prime(numbers):
    largest_prime = -1
    for n in numbers:
        if is_prime(n) and n > largest_prime:
            largest_prime = n
    return largest_prime

print(find_largest_prime([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

'''
given a list of numbers, find the one with most divisors
'''
def find_divisors(n):
    divisors = 0
    for i in range(1, n+1):
        if n % i == 0:
            divisors += 1

    return divisors

def solution(numbers):
    result = 0
    for n in numbers:
        if find_divisors(n) > result:
            result = n

    return result

f = open('example.txt', 'r')
content = f.readline()
print(content)
f.close()

f = open('example.txt', 'r')
count = 0
for col in f:
    print(col)
f.close()

f = open('example.txt', 'a')
f.write('Welcome to the class\n')
f.write('First line\n')
f.close()
