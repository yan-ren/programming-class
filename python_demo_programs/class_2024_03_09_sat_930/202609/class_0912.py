'''
algorithm 101

Searching & Sorting
'''

'''
linear search
binary search
'''

'''
given a list of numbers, and a target, find the target from the list
'''
def binary_search(list, target):
    low = 0
    high = len(list)-1

    while low <= high:
        mid = (low+high)//2

        if list[mid] == target:
            return mid
        elif list[mid] < target:
            low = mid+1
        else:
            high = mid-1

    return -1

numbers = [2, 5, 8, 12, 16, 23, 38, 45, 56, 72]
target = 23

print(binary_search(numbers, target))