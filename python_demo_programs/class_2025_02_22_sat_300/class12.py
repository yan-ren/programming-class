'''Favorite Fruits
Ask the user to enter favorite fruits and if enter 'exit' then stop

store them in a list, then print the list.

'''
from class_2025_02_22_sat_300.class2 import second

'''
more about list
'''

fruits = ["apple", "banana", "cherry"]
# fruits.append("orange")
fruits.insert(1, "orange")

# remove an element
fruits.remove("orange")
del fruits[0]

count = 0
numbers = [1, 2, 3, 1, 4, 2]

# if 2 in numbers:

for number in numbers:
    if number == 2:
        count += 1

print(count)

# if 2 in numbers:
# l1 = [1, 2]
# l2 = [3, 1, 4]
# l3 = []
#
# for num in l1:
#     l3.append(num)
#
# for num in l2:
#     l3.append(num)

# numbers = [1, 2, 3, 5, 4]
# max = numbers[0]
# second_max = numbers[0]
#
# for number in numbers:
#     if number > max:
#         second_max = max
#         max = number
#     elif number > second_max:
#         second_max = number

numbers = [3, 1, 4, 1, 5, 9, 2, 6]
numbers.sort(reverse=True)

new_numbers = sorted(numbers, reverse=True)

'''
common value

Given two list
l1 = [1, 2, 4]
l2 = [4, 5, 6]

There is one common value between l1 and l2. Find it
'''
'''
remove duplicate

l = [1, 2, 1, 3, 2, 4, 5]

remove duplicated value in list
output = [1, 2, 3, 4, 5]
'''