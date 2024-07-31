'''
Implementation of a modified binary search algorithm to find the
first occurrence of a specified value in a sorted list

[1, 2, 2, 2, 2, 3, 3, 4, 5, 6]
'''

def find_first_occurence(arr, target):
    low, high = 0, len(arr) - 1
    first_occurrence = -1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            first_occurrence = mid
            # high = mid - 1 # move to the left half
            low = mid + 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return first_occurrence

arr = [1, 2, 2, 2, 3, 4, 5]
print(find_first_occurence(arr, 1))