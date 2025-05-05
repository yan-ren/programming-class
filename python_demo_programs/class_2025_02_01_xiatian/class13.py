# i = 0
# while i <= 10:
#     print(i)
#     i += 1

# for i in range(10):
#     print(i)

# for i in range(1, 10, 2):
# for i in range(10, 0, -1):
#     print(i)

s = 'abc123!@##$%de'
# print(s[0]) # index
i = 0
while i < len(s):
    print(s[i])
    i += 1

for l in s:
    print(l)

# Print Even Numbers from 2 to 10
for i in range(2, 11, 2):
    print(i)

for i in range(2, 11):
    if i % 2 == 0:
        print(i)

s = 'abcde'
i = len(s) - 1

'''
FizzBuzz

Write a program that prints the numbers from 1 to 50, but:

If the number is divisible by 3, print "Fizz" instead.

If the number is divisible by 5, print "Buzz" instead.

If the number is divisible by both 3 and 5, print "FizzBuzz".

Otherwise, just print the number.
'''
