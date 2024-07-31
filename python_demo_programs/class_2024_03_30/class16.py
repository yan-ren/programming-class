'''
Two Sum

Given a list of integers nums and an integer target, return the indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

assume the list is sorted in accending order
'''

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