def bubble_sort(nums):
    n = len(nums)

    for i in range(n - 1):
        for j in range(n - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    return nums

numbers = [5, 3, 8, 4, 2]
print(numbers)
print(bubble_sort(numbers))