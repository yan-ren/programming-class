'''
12:30
'''
def get_digits(hour, minute):
    digits = []
    for ch in str(hour):
        digits.append(int(ch))
    digits.append(minute // 10)
    digits.append(minute % 10)

    return digits

def is_arithmetic(digits):
    if len(digits) < 3:
        return False

    diff = digits[1] - digits[0]
    for i in range(1, len(digits)):
        if digits[i] - digits[i-1] != diff:
            return False
    return True

print(get_digits(12, 30))