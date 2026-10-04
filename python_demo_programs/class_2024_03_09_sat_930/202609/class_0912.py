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

'''
variation:
find the first number position that is equal or larger than target
nums = [1, 3, 3, 5, 7, 9]
target = 3
output = 1, because index=1 has value 3 which is the first value bigger or larger than target

nums = [1, 3, 3, 5, 7, 9]
target = 4

output = 3
index 3 has value 5, which is the first value that is bigger or larger than target

nums = [2, 4, 6, 8]
target = 10
there is no number >= 10, so return len(nums)
'''

def lower_bound(nums, target):
    low = 0
    high = len(list)-1

    answer = len(nums)

    while low <= high:
        mid = (low+high)//2
        if nums[mid] >= target:
            answer = mid
            high = mid - 1
        else:
            low = mid + 1

    return answer


nums = [1, 3, 3, 5, 7, 9]
print(nums.index(5))