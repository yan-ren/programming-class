def is_prime(n):
    if n < 2:
        return False
    div = 2
    while div < n:
        if n % div == 0:
            return False
        div += 1
    return True


# number = 2
# while number <= 100:
#     if is_prime(number):
#         print(number)
#     number += 1

s = 'aaaaabca'
t = 'def'
# w = s * 3
# print(w)
#
# upper_s = s.upper()
# print(upper_s)
# print(upper_s.lower())
#
# print(s.replace('a', 'aa'))
# print(s.count('a'))

print(s.find('bc'))
print(s.find('we'))

s = 'bananas'
for c in s:
    if c in 'aeiou':
        print(c, end='#')