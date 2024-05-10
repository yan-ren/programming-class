'''
Given a string, count how many vowels inside?
'''

s = 'success'
counter = 0
for letter in s:
    # if letter == 'a' or letter == 'e' or letter == 'o' or letter == 'i' or letter == 'u':
    if letter in ['a', 'e', 'i', 'o', 'u']:
        counter += 1

print(counter)

