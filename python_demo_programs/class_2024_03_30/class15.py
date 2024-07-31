'''
bubble sort
'''
import math


def bubble_sort(arr):
    N = len(arr)

    for i in range(N):
        swapped = False
        for index in range(N-1):
            # if math.abs(arr[index]) > math.abs(arr[index + 1]):
            if compare_abs(arr[index], arr[index + 1]) == 1:
                arr[index], arr[index + 1] = arr[index + 1], arr[index]
                swapped = True

        if not swapped:
            break


arr = [5, 4, 3, 2, 1]
bubble_sort(arr)
print(arr)

'''
exercise: sort list by absolute values using bubble sort
given a list of numbers, which can be both positive and negative, sort the number base on their absolute value 
using bubble sort

e.g.
input: [-7, 2, -3, 8, -2, 5, -8, 1, -1, 4, 0]
output: [0, 1, -1, 2, -2, -3, 4, 5, -7, 8, -8]
'''
'''
return 1 if abs(a1) > abs(a2)
return 0 if abs(a1) == abs(a2)
return -1 if abs(a1) < abs(a2)
'''
def compare_abs(a1, a2):
    if a1 < 0:
        a1 *= -1
    if a2 < 0:
        a2 *= -1

    if a1 > a2:
        return 1
    elif a1 < a2:
        return -1
    return 0

