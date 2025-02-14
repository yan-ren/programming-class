'''
int
float
boolean
string
'''

s = 'it good'
# print(len(s))
#
# i = 0
# while i < len(s):
#     print(s[i])
#     i += 1
#
# i = 0
# for i in range(len(s)):
#     print(s[i])
#
# for i in s:
#     print(i)

# print(s[6])
# print(s[-1])
# print(s[len(s) - 1])

l = [1, 2, 34, 29]
l.append(10)
print(l)
print(max(l))
l.sort(reverse=True)
print(sum(l))
print(l.count(1))
# print(l.index(340))
# if 340 in l:
#     print(l.index(340))

# s = 'abcd'
#
# if 'bc' in s:
#     print('bc is in string s')

print('''
Menu:
1. Determine the amount of water needed to fill the pool
2. Determine the time needed to fill the pool
3. Determine the time needed to drain the pool
4. Add water for a specific amount of time
5. Drain water for a specific amount of time
6. Display current pool status
7. Exit
''')

number = 12.22522
# print('{:.2f}'.format(number))
# print(round(number, 2))

print(int(number * 100) / 100)