'''
more about for loop
- range
- list
- string
'''

# calculate the sum from 1 to 100
# hint: using range and for loop to go through 1 to 100, and add them up
# sum = 0
# for num in range(1, 101):
#     sum += num
#
# print(sum)

# number = [1, 2, 1, 2, 5, 23, 5]
# new_number = []
# exercise: filter out even number only keep the odd number
# for num in number:
#     if num % 2 != 0:
#         new_number.append(num)

# string can also be used with for loop
# s = 'abcdef'
# index = 0
# while index < len(s):
#     print(s[index])
#     index += 1
#
# for ch in s:
#     print(ch)

# nested loop
# for i in range(4):
#     for j in range(4):
#         print(j)

# break, continue, they still work in for loop, same as while loop
# for i in range(5):
#     if i == 2:
#         continue
#     print(i)

# given a string of letters, find how many vowels, e.g. aeiou
# s = 'WELCOME'
# count = 0
#
# for letter in s.lower():
#     # how to check if it's vowel?
#     if letter in 'aeiou':
#         count += 1
#
# print(count)

numbers = [[1, 2, 1, 2], [2, 3, 5], [3, 2, 1]]
# how to loop all numbers using for loop?
for sub in numbers:
    for num in sub:
        print(num)

# homework: given a list of numbers, calculate the sum of even number and sum of odd number
'''
numbers = [1, 2, 4, 2]

sum of even: 8
sum of odd: 1
'''
count_even = 0
count_odd = 0

for num in numbers:
    if num % 2 == 0:
        count_even += 1
    else:
        count_odd += 1

print(count_even, count_odd)