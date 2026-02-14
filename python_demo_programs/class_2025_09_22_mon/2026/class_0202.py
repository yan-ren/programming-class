# names = ['Tom', 'Jerry', 'Tim'] # length is 3, but the index is 0, 1, 2
#
# print(names[0])

# index = 0
# while index < len(names):
#     print(names[index])
#     index += 1

# for n in names:
#     print(n)

# exercise: given a list of names, print all the names that is longer than 5 letters
# names = ['Prashant', 'Tom', 'Jerry', 'Tim', 'Cherry']
# print Prashant, Cherry
# hint: use loop and if statement
# names = ['Prashant', 'Tom', 'Jerry', 'Tim', 'Cherry']
#
# for name in names:
#     if len(name) > 5:
#         print(name)

# numbers = [1, 2, 1, 5, 3, 4]
#
# numbers.sort()
# print(numbers)
#
# numbers.sort(reverse = True)
#
# print(max(numbers))
# print(min(numbers))
#
# print(numbers.count(1))
#
# names = ['Prashant', 'Tom', 'Jerry', 'Tim', 'Cherry']
# print(names.index('Tim'))

# next class: build a memorization game using list, loop, etc

# homework:
'''
Given a list of number with positive and negative value, create a new one by keeping only
the positive value

numbers = [-1, 2, -3, 1]
new_numbers = [2, 1]
'''
numbers = [-1, 2, -3, 1]
new_number = []

for num in numbers:
    if num > 0:
        new_number.append(num)

print(new_number)