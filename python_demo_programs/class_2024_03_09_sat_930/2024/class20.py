'''
Write a python function that calculates the sum of all even numbers in a list

e.g.

input: [2, 1, 4, 2, 5, 3]
output: 8
'''

def sum_even(list):
    res = 0
    for value in list:
        if value % 2 == 0:
            res += value

    return res


# loop forward
for i in range(0, 10):
    print(i)

# loop backward
for i in range(10, 0, -1):
    print(i)

for i in range(10, 0, -2):
    print(i)

numbers = [1, 3, 2, 6, 5]
# numbers.sort()
# print(numbers)
# numbers.reverse()
# print(numbers)
numbers.sort()
numbers.reverse()
print(numbers)

# find the largest value, or find the second largest value from the list
# use sorting

def find_max(numbers):
    if len(numbers) == 0:
        return None

    numbers.sort()

    return numbers[len(numbers) - 1]