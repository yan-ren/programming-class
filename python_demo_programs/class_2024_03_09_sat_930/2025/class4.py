'''
2015 J3
'''
def is_consonant(ch):
    vowels = 'aeiou'
    if ch not in vowels:
        return True

    return False


def closest_vowel(ch):
    vowels = 'aeiou'
    min_diff = float('inf')
    closest = ''

    for v in vowels:
        diff = abs(ord(ch) - ord(v))
        if diff < min_diff:
            min_diff = diff
            closest = v

    return closest


def next_consonant(ch):
    if ch == 'z':
        return ch

    next_ch = chr(ord(ch) + 1)
    while next_ch in 'aeiou':
        next_ch = chr(ord(next_ch) + 1)

    return next_ch

sample = input()
output = ''

for ch in sample:
    if not is_consonant(ch):
        output += ch
    else:
        output += (ch + closest_vowel(ch) + next_consonant(ch))

print(output)