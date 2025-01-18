'''list method
sort
count
index: returns the index of the first element with the specified value
'''

numbers = [1, 2, 1, 4, 4, 2]
# print(numbers.count(4))

def count(numbers, target):
    counter = 0
    for num in numbers:
        if num == target:
            counter += 1

    return counter


print(count(numbers, 4))

print(numbers.index(4))

def index(numbers, target):
    position = 0

    for value in numbers:
        if value == target:
            return position
        position += 1

    return None


print(index([1, 2, 3, 4], 4))
print(index([1, 2, 3, 4], 1))

'''
find the index of the last occurrence in a list of number
e.g. [1, 2, 3, 3, 3, 4, 1], find 3
return 4
'''
# solution 1
def find_last_occurrence(numbers, target):
    numbers.reverse()

    index = 0
    while index < len(numbers):
        if numbers[index] == target:
            return index

        index += 1

    return -1

# solution 2
def find_last_occurrence(numbers, target):
    index = len(numbers) - 1
    while index >= 0:
        if numbers[index] == target:
            return index
        index -= 1

    return -1

# solution 3
def find_last_occurrence(numbers, target):
    index = 0
    last_index = -1

    while index < len(numbers):
        # ????
        if numbers[index] == target:
            last_index = index

        index += 1

    return last_index

