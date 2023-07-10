def two_sum(nums, target):
    nums.sort()

    left = 0
    right = len(nums) - 1

    while left < right:
        sum = nums[left] + nums[right]
        if sum > target:
            right -= 1
        elif sum < target:
            left += 1
        else:
            return [nums[left], nums[right]]


print(two_sum([2,7,11,15], 9))
print(two_sum([3,2,4], 6))
