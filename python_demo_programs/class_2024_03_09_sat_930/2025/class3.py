'''
2026 J3
'''

longest = ''

sample = input()

def expand_from_center(left, right):
    while left >= 0 and right < len(sample) and sample[left] == sample[right]:
        left -= 1
        right += 1

    return sample[left + 1:right]


for i in range(len(sample)):
    option1 = expand_from_center(i, i)
    option2 = expand_from_center(i, i+1)

    if len(option1) > len(longest):
        longest = option1
    if len(option2) > len(longest):
        longest = option2

print(len(longest))