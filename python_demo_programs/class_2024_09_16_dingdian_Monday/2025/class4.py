'''
https://dmoj.ca/problem/ccc12j2
'''
from typing import List


# numbers = []
#
# for i in range(4):
#     numbers.append(int(input()))

# if numbers[0] == numbers[1] and numbers[1] == numbers[2] and numbers[2] == numbers[3]:


def countSubarrays(nums: List[int], k: int) -> int:
    max_element = max(nums)
    count = {}
    ans = 0
    left = 0

    for right in range(len(nums)):
        if nums[right] in count:
            count[nums[right]] += 1
        else:
            count[nums[right]] = 1

        if count.get(max_element, 0) < k:
            continue

        while count[max_element] >= k:
            print(left, right)
            ans += 1
            count[nums[left]] -= 1
            left += 1

    return ans

print(countSubarrays([1,3,2,3,3], 2))