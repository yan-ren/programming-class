# s = 'abcde'
# print(s.count('a'))
# s = '12341'

# version 1
def find_duplicate(s):
    for ch in s:
        if s.count(ch) > 1:
            return True

    return False

# version 2
# def find_duplicated(s):
#     i = 0
#     while i < len(s):
#         j = i + 1
#         while j < len(s):
#             if s[i] == s[j]:
#                 return True
#         j += 1
#     i += 1
#     return False

# start = int(input())
# start += 1
#
# while True:
#     if find_duplicate(str(start)): # 123 -> '123'
#         print(start)
#         break
#     else:
#         start += 1

line1 = '*x*'
line2 = ' xx'
line3 = '* *'

k = int(input())

new_line1 = ''
for ch in line1:
    new_line1 += ch * k

for _ in range(k):
    print(new_line1)