import math


def pi_series(n):
    result = 0
    for k in range(n):
        result += 2 * (-1)**k * 3 ** (1/2 - k) / (2 * k + 1)

    return result


# print(pi_series(30))
# print(math.pi)
number = pi_series(30)
print(number)
num_str = str(number)
number = float(num_str[:num_str.find('.') + 3])
print(number)

number = 123124.1231231
print(number)
num_str = str(number)
number = float(num_str[:num_str.find(".") + 3])
print(number)

print(round(3.14159, 4))

def distance(u, v):
    return round(math.sqrt((u[0] - v[0])**2 + (u[1] - v[1])**2), 2)

def count_stop(dna):
    if len(dna) % 3 != 0:
        return -1

    count = 0

    for i in range(0, len(dna), 3):
        if dna[i:i+3] == 'TAG' or dna[i:i+3] == 'TAA' or dna[i:i+3] == 'TGA':
            count += 1

    return count


print( count_stop ("TACACTTAACCCTAG"))
print( count_stop ("TGATG"))
print( count_stop ("TTTTATTGACCACGAGATTTATGAATTTACTAGACT"))

def validPass(password):
    if ' ' in password:
        return False

    if len(password) < 10:
        return False

    if len(password) < 16:
        has_digit = False
        has_special = False
        special_chars = '$*&%#'

        for char in password:
            if char in '0123456789':
                has_digit = True
            if char in special_chars:
                has_special = True

        if has_special and has_digit:
            return True
        else:
            return False

    return True