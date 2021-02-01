# question1: create a list with numbers from square of 1 to square of 9
# [1, 4, ... 81]
# approach:
# 1. create new list
# 2. loop
# 3. inside the loop, put the value into new list base on conditions
# list = []
# for i in range(1, 10):
#     list.append(i*i)
#
# question2: given a list of numbers, create a new list with only even numbers from the given list
# example [1, 2, 3, 4, 5] -> [2, 4]
# approach:
# 1. create new list
# 2. loop through the given list
# 3. inside the loop, put the value into new list base on conditions
list = []
for i in [1, 2, 3, 4, 5]:
    if i % 2 == 0:
        list.append(i)
# comprehension
[i for i in [1, 2, 3, 4, 5] if i % 2 == 0]

# question3: given a list of numbers, create a new list with only positive numbers from the given list
list = []
for i in [1, 2, 3, -4, 5]:
    if i > 0:
        list.append(i)

# list comprehension
a = [i for i in [1, 2, 3, -4, 5] if i > 0]
print(a)
