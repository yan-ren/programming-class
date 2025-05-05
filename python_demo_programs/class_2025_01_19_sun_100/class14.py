'''
Exercise:
write a program ask user for two numbers, num1 and num2
where num1 < num2
calculate the sum from num1, num1 + 1, num1 + 2, ..., num2

e.g.
num1 = 20
num2 = 30
result = 20 + 21 + 22 + ... + 30
'''

# num1 = int(input('Enter the first number:'))
# num2 = int(input('Enter the second number:'))
#
# result = 0
# i = num1
#
# while i <= num2:
#     result += i
#     i += 1
#
# print(result)

# for i in range(10):
#     print(i)

# for i in range(5, 10):
#     print(i)
#
# for i in range(2, 10, 2):
#     print(i)
#
# for i in range(9, 0, -1):
#     print(i)
# s = 0
# for i in range(1, 101):
#     s += i
#
# print(s)
s = 'abcdef'
for i in s:
    print(i)

i= 0
while i < len(s):
    print(s[i])
    i += 1

'''
Write a program ask people a word, then print the word in reversed order
hint: use loop

example:
people type: hello
you print: olleh
'''
