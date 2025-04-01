import random
from helper import check_prime

def two_primes(a):
    lower = 2 ** (a - 1)
    upper = 2 ** a

    first = None
    second = None

    while first is None:
        candidate = random.randint(lower, upper)
        if check_prime(candidate):
            first = candidate

    while second is None:
        candidate = random.randint(lower, upper)
        if check_prime(candidate) and candidate != first:
            second = candidate

    return first, second