def sum_multiples(n):
    result = []
    for i in range(n + 1):
        if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
            result.append(i)

    return sum(result)
