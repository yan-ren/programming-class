'''
String

character: abc1234!@#$
'''

# s = ''
# print(type(s))
# print(len(s))
#
# s = 'abc123'
# print(len(s))
#
# s = 'He said: "The answer is 42"'
# s = '''He said: "yes, it’s 42"'''
# print(s)

greeting = 'hello'
group = 'world'

res = greeting + ' ' + group
print(res)

s = 'Arthur'
# print(s[0])
# print(len(s) - 1)
# print(s[len(s) - 1])
# print(s[-1])
# print(s[2])
# print(s[-4])

# largest index = length - 1

# string slicing
# print(s[0:2])
# print(s[:2])
#
# print(s[1:])
# print(s)

# print(s * 3)
#
# a = False
# b = False
# print(type(a))
# print(type(b))

# and, as long as one side is False, overall is False
# print(a and b)
#
# # or, as long as one side is True, overall is True
# print(a or b)
#
# # not, reverse
# print(not (a and b))

x = 2
y = 2
# print(x > y)
# print(y > x)
# print(x == y)
# print(x != y)

# conditional
if x > y:
    print('x is bigger')
elif x < y:
    print('y is bigger')
else:
    print('same')

x = int(input('Enter a number to check positive, negative, or zero: '))
if x > 0:
    print('x is positive')
elif x < 0:
    print('x is negative')
else:
    print('x is zero')

