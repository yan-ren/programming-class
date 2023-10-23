'''
Given an array of sorted numbers, 
remove all duplicate from it. (using two pointer approach, O(N))

Input: [2, 3, 3, 3, 6, 9, 9]
Ouput: [2, 3, 6, 9]
'''

def remove_duplicates(arr):
    if len(arr) < 1:
        return arr
    
    next_non_duplicate = 1
    next = 1

    while next < len(arr):
        if arr[next_non_duplicate - 1] != arr[next]:
            arr[next_non_duplicate] = arr[next]
            next_non_duplicate += 1
        next += 1

    return arr[:next_non_duplicate]

