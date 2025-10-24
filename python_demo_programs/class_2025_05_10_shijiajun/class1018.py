'''
3. Write a loop that calculates the total of the following series of numbers:
(1 / 50) + (2 / 49) + (3 / 48) + (4 / 47) + ...+ (48 / 3) + (49 / 2) + (50 / 1)
'''
# numerator = 1
# result = 0
#
# while numerator <= 50:
#     result = result + (numerator / (51 - numerator))
#     numerator += 1
#
# print(result)

# range(10) # 0, 1, 2, 3, ...9

# for i in range(1, 10, 2):
#     print(i)

# 1+2+3+4+..+10
# i = 1
# result = 0
#
# while i <= 10:
#     result = result + i
#     i += 1
#
# print(result)

# result = 0
# for i in range(11):
#     result = result + i

# s = 'abcde'
#
# for ch in s:
#     print(ch)

# result = 0
# for i in range(1, 51):
#     result = result + (i / (51 - i))
#
# print(result)
s = 'abc'

i = 0
s_reverse = ''
while i < len(s):
    s_reverse = s[i] + s_reverse
    i += 1

print(s_reverse)


s_reverse = ''
for ch in s:
    s_reverse = ch + s_reverse

print(s_reverse)

# given a string, count how many vowels, using for loop
