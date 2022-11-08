# basic solution
'''
start from every index of the given array and add the next k element to find the sum
'''
from threading import local


def max_sublist_1(list, k):
    max_sum = 0
    
    for i in range(len(list) - k + 1):
        local_sum = 0
        # add next k numbers
        for j in range(i, i + k):
            local_sum += list[j]
        
        max_sum = max(max_sum, local_sum)
    
    return max_sum

print(max_sublist_1([2, 1, 5, 1, 3, 2], 3))

def max_sublist_2(list, k):
    max_sum, window_sum = 0, 0
    start = 0

    for end in range(len(list)):
        window_sum += list[end]
        if end >= k - 1:
            max_sum = max(max_sum, window_sum)
            # subtract the first value from window
            window_sum -= list[start]
            start += 1

    return max_sum

print(max_sublist_2([2, 1, 5, 1, 3, 2], 3))

