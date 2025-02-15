text = 'abcd'
text_reverse = ''

for ch in text:
    text_reverse = ch + text_reverse

    '''
    1.
    text_reverse = 'a'
    
    2. ch = 'b'
    
    ch + text_reverse
    'b' + 'a'
    text_reverse = 'ba'
    
    3. ch = 'c'
    ch + text_reverse
    'c' + 'ba'
    text_reverse = 'cba'
    '''

# for i in range(10): # [0, 9]
#     print(i)
#
# s = 'abc'
# for i in s:
#     print(i)
#
#
# i = 0
# while i < len(s):
#     print(s[i])
#     i += 1

# nested loop
# for row in range(5):
#     for col in range(5):
#         print('*', end='')
#     print()

# how to print all even number under 100
# i = 0
# while i < 100:
#     if i % 2 == 0:
#         print(i)
#     i += 1
#
# i = 0
# while i < 100:
#     i += 2
#     print(i)
#
# for i in range(0, 100, 2): # start from 0, stop at 100 (not included),
#     print(i)               # each time increment by 2
#
# for i in range(100):
#     if i % 2 == 0:
#         print(i)
#
# # how to calculate the sum of all even numbers under 100
# i = 0
# s = 0
# while i < 100:
#     if i % 2 == 0:
#         s += i
#     i += 1

a = 1
b = 1

for i in range(1, 100):
    if i == 1 or i == 2:
        print(i)
    next = a + b
    print(next)
    a = b
    b = next