'''
2024 J4
'''
s1 = input()
s2 = input()

# find the silly key in s2
# which means a letter in s2 but not in s1
wrong = ''

for ch in s2:
    if ch not in s1:
        wrong = ch

i = 0
j = 0
silly = ''
quiet = ''
while i < len(s1) and j < len(s2):
    if s1[i] == s2[j]:
        i += 1
        j += 1
    elif s2[j] == wrong:
        silly = s1[i]
        i += 1
        j += 1
    else:
        quiet = s1[i]
        i += 1

while i < len(s1):
    if quiet == '':
        quiet = s1[i]
    i += 1

print(silly, wrong)
if quiet:
    print(quiet)
else:
    print('-')