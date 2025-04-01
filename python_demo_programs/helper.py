import math
import random

def check_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def list_primes(a, b):
    primes = []
    for num in range(2**a, 2**b):
        if check_prime(num):
            primes.append(num)
    return primes
