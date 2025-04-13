'''
Data Structure
- List
- Dictionary
- Set

Algorithm
- Search: Find an item from a list
- Sequential Search
- Binary Search
'''
# target = 200
# numbers = [2, 1, 4, 20, 10]
#
# print(numbers.index(target))

# loop through each element in the list, compare,
# if find the target, return the index, if not found, return None
'''
best case: if the target is at the first place
worse case:if the target is not in the list
'''
def sequential_search(numbers, target):
    # index = 0
    # while index < len(numbers):
    #     if numbers[index] == target:
    #         return index
    #
    # return None

    for i in range(len(numbers)):
        if numbers[i] == target:
            return i

    return None

'''
binary search: precondition, all elements in list are sorted 
'''
def binary_search(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left <= right:
        mid = (left + right) // 2
        if numbers[mid] == target:
            return mid
        elif numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return None

print(binary_search([1, 3, 4, 6, 9, 12], 1))
