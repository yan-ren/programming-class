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

# [1, 3, 5]
def is_arithmetic(digits):
    if len(digits) < 3:
        return False

    diff = digits[1] - digits[0]
    for i in range(1, len(digits)):
        if digits[i] - digits[i-1] != diff:
            return False
    return True

favourite_minute = []
for t in range(720):
    hour = (t // 60) % 12
    if hour == 0:
        hour = 12
    minute = t % 60

    if is_arithmetic(get_digits(hour, minute)):
        favourite_minute.append(t)

D = int(input())
cycle = 720
count = (D // 720) * len(favourite_minute)

remaining = D % cycle
for t in favourite_minute:
    if t <= remaining:
        count += 1

print(count)