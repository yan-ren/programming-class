'''
Two Sum

Given a list of integers nums and an integer target, return the indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

assume the list is sorted in accending order
'''
from typing import List


def two_sum(num, target):
    i = 0
    j = len(num) - 1

    while i < j:
        if num[i] + num[j] == target:
            return i, j
        elif num[i] + num[j] > target:
            j -= 1
        else:
            i += 1

    return -1, -1


'''
exercise: selection sort

insertion sort
'''
def insertion_sort(num):
    # loop from index 1 to len(arr) - 1
    for i in range(1, len(num)):
        j = i
        while j > 0 and num[j-1] > num[j]:
            num[j], num[j-1] = num[j-1], num[j]
            j -= 1

    return num

'''
exercise: find the peak element in an unsorted list
Given a list of integers, find a peak element. A peak element is an element that is strictly greater than its neighbors. 
If the list contains multiple peaks, return the index of any one of them.

list = [1, 2, 3, 1]
'''
# def find_peak_element(numbers):

def find_peak_element(numbers: List[int]) -> int:
    left, right = 0, len(numbers) - 1
    while left < right:
        mid = (left + right) // 2

        if numbers[mid] < numbers[mid+1]:
            # if the middle element is less that the mid + 1
            # peak element is in the right half
            left = mid + 1
        elif numbers[mid] < numbers[mid-1]:
            right = mid - 1
        else:
            return mid

    return left

print(find_peak_element([1, 2, 3, 1]))
print(find_peak_element([1, 2, 1, 3, 5, 6, 4]))
