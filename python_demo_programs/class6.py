'''
Cover slide: day 07

Topic: string

A string is a sequence of zero or more characters. String are delimited by single or double quotes.

note: zero or more
character: letter, number and special symbol. e.g. abc123!@#$

'''
# s = 'abc123!@#'
# s = 'he said:"the anser is 42"'
# s = ''

# string concatenation
# a = '1'
# b = '2'
# print(a + b)
#
# greeting = 'hello'
# group = 'world'
# print(greeting + " " + group)

# String indexing
# s = 'Arthur'
# print(s[0])
# String length = the number of character in string
# print(len(s))
# print(s[-1])

# s_new = s[0:2]
# s_new = s[:2]
# print(s_new)
# print(s)
# print(s[1:5:2])
# print(s[::-1])

# question: what's the relation between len vs largest index
# largest_index = len() - 1
# s = 'welcome'
# i = 0
# count = 0
# while i < len(s):
#     # print(s[i])
#     if s[i] == 'e':
#         count += 1
#     i += 1
#
# print('The number of e', count)


'''
Exercise 1
Ask Until Positive Number
Ask the user to enter a number. If they enter a negative number, keep asking until they enter a positive one.
Hint: input()
'''
# while True:
#     number = int(input('Enter a positive number:'))
#     if number > 0:
#         break
#     print('The number not positive, try again')

# running = True
# while running:
#     number = int(input('Enter a positive number:'))
#     if number > 0:
#         running = False
#     else:
#         print('The number is not positive, try again')
'''
Exercise 2
Counting Down
Ash the user to enter a positive number. Counting down from this positive number to zero
e.g. user enters 5
should print
5
4
3
2
1
0
'''
# running = True
# number = 0
# while running:
#     number = int(input('Enter a positive number:'))
#     if number > 0:
#         running = False
#     else:
#         print('The number is not positive, try again')
#
# while number >= 0:
#     print(number)
#     number -= 1

s = 'welcome'
# i = 0
# while i < len(s):
#     print(s[i])
#     i += 1

for ch in s:
    print(ch)

# range(10): 0, 1, 3, 4, ... 9
for i in range(10):
    print(i)

for i in range(1, 10):
    print(i)

for i in range(1, 10, 2):
    print(i)

# how to calculate 1 + 2 + 3 + ... 100 using for loop?
# s = 0
# for i in range(1, 101):
#     s += i
# print(s)

'''
Exercise: ask user for a word and count how many vowels in the word
e.g. hello -> 2
'''
word = input('Enter a word:')
count = 0

for ch in word:
    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
        count += 1

print(count)

index = 0
count = 0
while index < len(word):
    if word[index] == 'a' or word[index] == 'e' or word[index] == 'i' or word[index] == 'o' or word[index] == 'u':
        count += 1
    index += 1
    