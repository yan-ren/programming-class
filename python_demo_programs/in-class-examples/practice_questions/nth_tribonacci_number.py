def nth_tribonacci_number(n):
    t0 = 0
    t1 = 1
    t2 = 1

    if n == 0:
        return t0
    if n == 1:
        return t1
    if n == 2:
        return t2

    index = 0
    while index < n - 2:
        next_value = t0 + t1 + t2
        t0 = t1
        t1 = t2
        t2 = next
        index += 1

    return next_value


def nth_tribonacci_number_recursive(n):
    # base case
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1

    return nth_tribonacci_number_recursive(n - 1) + nth_tribonacci_number_recursive(n - 2) \
        + nth_tribonacci_number_recursive(n - 3)


'''
usually recursive approach involves many repetitive steps, e.g. same number calculate multiple times
this is a quite common case
one way to optimize recursive solution is using "memorization", in other name is also called "dynamic programming"
'''