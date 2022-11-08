def canThreePartsEqualSum(l):
    if sum(l) % 3 != 0:
        return False

    partial_sum = sum(l) / 3
    current = 0
    counter = 0

    for i in l:
        current += i
        if current == partial_sum:
            counter += 1
            current = 0

    return counter >= 3

# [0, 0, 0, 0]