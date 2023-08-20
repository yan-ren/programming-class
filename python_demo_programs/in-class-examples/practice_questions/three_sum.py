def three_sum(nums):
    result = []

    nums.sort()

    # first loop
    i = 0
    while i < len(nums) - 2:
        # edge case: skip the duplicate in first loop
        while i < len(nums) - 2 and nums[i] == nums[i-1]:
            i += 1

        red = nums[i]
        left = i + 1
        right = len(nums) - 1
        while left < right:
            # if match found
            if red + nums[left] + nums[right] == 0:
                result.append([red, nums[left], nums[right]])
                left += 1
                right -= 1
                # if left pointer is the same as previous value, skip
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                # if right pointer is the same as previous value, skip
                while left < right and nums[right] == nums[right + 1]:
                    right += 1
            # if sum is bigger than zero, increase the left pointer
            elif red + nums[left] + nums[right] > 0:
                right -=1
            # if sum is smaller than zero, decrease the right pointer
            else:
                left += 1

        i += 1

    return result


print(three_sum([-1,0,1,2,-1,-4]))
print(three_sum([0,0,0]))


s = set()
s.add((-1, 0, 1))
print((-1, 0, 1) in s)