'''
strategy: negate minimum each time, overall sum is maximum

case1: when all numbers are positive

no matter which value being negate, always get negative value

case2: when have negative and positive value

the value being negated is the min negative, so we get a large positive
'''

def largestSumAfterKNegation(nums, k):
    for i in range(k):
        # find the index of minimum value
        min_index = nums.index(min(nums))
        nums[min_index] = -nums[min_index]

    return sum(nums)
