'''
while
for

for xx in range()/string:

list

'''

# students = ['Tom', 'Jerry', 'Jack']
# numbers = [1, 2, 1, 3]
# l = ['Tom', 1, True]

numbers = [2]
numbers.append(1)
print(numbers)

# list has index starting from 0
print(numbers[0])

# delete by index
del numbers[0]
numbers.remove(1) # remove the first value 1 from the left

# exercise: given a list of numbers, loop each value one by one
numbers = [1, 2, 1, 4, 2, 5]

# # while
# index = 0
# while index < len(numbers):
#     print(numbers[index])
#     if numbers[index] == 1:
#         numbers[index] = 0
#     index += 1
#
# # for
# for num in numbers:
#     print(num)

# exercise: given a list of number, find the maximum number from the list
numbers = [-1, -2, -1, -4, -2, -5]

# max_number = numbers[0]
#
# for n in numbers:
#     if n > max_number:
#         max_number = n
#
# print(max(numbers), min(numbers))

'''
Homework

Given a list of numbers, 
create a new list only with the positive numbers from the original list
hint: use loop and append

given: [1, 2, -1, 4, -3]
new: [1, 2, 4]


Given a list of words, create a new list containing only the words 
that have more than 3 characters.

Example:
Given: ["cat", "elephant", "dog", "horse", "ant"]
New: ["elephant", "horse"]
'''
numbers = [1, 2, -1, 4, -3]
new_numbers = []

for num in numbers:
    if num > 0:
        new_numbers.append(num)


text = ['cat', 'elephant', 'dog', 'horse', 'ant']
new_text = []

for s in new_text:
    if len(s) > 3:
        new_text.append(s)


