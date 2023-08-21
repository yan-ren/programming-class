'''
https://leetcode.com/problems/number-of-distinct-averages/
'''
def distinctAverages(nums: list[int]) -> int:
    nums.sort()
    # new_nums = sorted(nums)

    result = set()

    index = 0
    while index < len(nums) / 2:
        result.add((nums[index] + nums[len(nums) - index - 1]) / 2)
        index += 1

    return len(result)


print(distinctAverages([4,1,4,0,3,5]))
