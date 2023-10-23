'''
Question
Given a list of sorted numbers and a target sum, 
find a pair in the list whose sum is equal to the given target.
'''

def pair_with_target_sum(arr, target_sum):
    left, right = 0, len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target_sum:
            return [arr[left], arr[right]]
        
        if target_sum > current_sum:
            left += 1 # move the left pointer to get a bigger sum
        else:
            right -= 1 # move the right pointer to get a smaller sum

    return None

print(pair_with_target_sum([1, 2, 3, 4, 6], 6))
