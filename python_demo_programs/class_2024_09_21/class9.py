'''
while loop is more generic
for loop
only iterable item can be put after 'in' keyword
'''

# s = 'hello'
# index = 0
# while index < len(s):
#     print(s[index])
#     index += 1
#
# for ch in s:
#     print(ch)


# index = 0
# while index < 10:
#     print(index)
#     index += 1

# for i in range(10):
#     print(i)

'''
Sum of Numbers:
Write a program that calculates the sum of numbers from 1 to 100 using a for loop.
'''
s = 0
for i in range(101):
    s += i
'''
Reverse a String:
Write a program that prints a string in reverse using a for loop.
Example:
Input: "Python"
Output: "nohtyP"
'''
# s = 'Python'
# s_new = ''
#
# for letter in s:
#     s_new = letter + s_new

'''
multiplication table
1x1 = 1
2x1 = 2
2x2 = 4
3x1 = 3
3x2 = 6
3x3 = 9
...
'''
for i in range(1, 10):
    # i x j
    for j in range(1, i+1):
        # print(str(i) + ' * ' + str(j) + ' = ' + str(i*j))
        print('*', end='')

    print()