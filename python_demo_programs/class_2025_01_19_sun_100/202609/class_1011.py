# scores = []
#
# for i in range(5):
#     scores.append(int(input()))
#
# scores.remove(max(scores))
# scores.remove(min(scores))
#
# print(sum(scores) * int(input()))

'''
dmoj
Username: ryanacademy
Password: 1275canadian
'''

'''
Part 1 - Python list review
'''
numbers = [5, 2, 8, 1, 9]

print(numbers[0])
print(numbers[-1])
print(numbers[1:4])
print(numbers[::-1])

nums = [4, 2, 7, 2]
nums.append(9)
print(nums) # [4, 2, 7, 2, 9]

nums.remove(2)
print(nums) # [4, 7, 2, 9]

nums.pop() # [4, 7, 2] remove the right most value
print(nums)
nums.insert(1, 10) # [4, 10, 7, 2]

nums.sort() # [2, 4, 7, 10]

nums.reverse() # [10, 7, 4, 2]

print(nums.count(4)) # 1
print(nums.index(7)) # ???

nums = [1, 2, 2, 3, 2, 4]
for x in nums:
    print(x, nums.count(x))

