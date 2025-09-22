# number = int(input('Enter a number:'))
# print('You entered:', number)
#
# if number % 2 == 0:
#     if number > 0:
#         print('Positive Even')
#     else:
#         print('Non positive even')
# else:
#     if number > 0:
#         print('Positive Odd')
#     else:
#         print('Non positive odd')

# exercise: as user for a letter, check if it's vowel or not?
# letter = input('Enter a letter:')
# if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
#     print('vowel')
# else:
#     print('not vowel')

# if letter in 'aeiou':
#     print('vowel')
# else:
#     print('not vowel')

# age = int(input("Enter your age: "))
# # 0-13, 13-20, 20-60, > 60
# if age < 13:
#     print('You are a child')
# elif age < 20:
#     print('You are a teenager')
# elif age < 60:
#     print('You are an adult')
# else:
#     print('You are a senior')

# i = 1
# while i <= 10:
#     print(i)
#     i = i + 1

# 10, 9, 8, ..., 1
i = 10
while i > 0:
    print(i)
    # i = i - 1
    i -= 1

# how to calculate 1 + 2 + 3 + ... + 100, using while loop
# i = 1
# s = 0
# while i <= 100:
#     s = s + i
#     i = i + 1
#
# print(s)

i = 2
s = 0
while i <= 100:
    s += i
    i += 2

print(s)

i = 1
s = 0
while i <= 100:
    if i % 2 == 0:
        s += i
    i += 1

print(s)