'''
list
dictionary
set
'''
s = set()
s.add(1)
s.add(2)
print(s)
s.add(1)
print(s)

s = {1, 2, 3, 4}
# if 5 in s:
numbers = [1, 2, 3, 4, 2]

s = set(numbers)

chars = set("hello")
print(chars)

evens = set(range(0, 10, 2))
print(evens)

chars.remove('h')

a = {1, 2}
b = {2, 3}
print(a | b)
print(a & b)
print(a - b)
print(a ^ b)

'''
Given an integer array nums, return True if any value appears at least twice, and False if every element is distinct.
Example 1
Input:  nums = [1, 2, 3, 1]
Output: True
Example 2
Input:  nums = [1, 2, 3, 4]
Output: False
'''

'''
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique.
Example 1
Input:  nums1 = [1,2,2,1],  nums2 = [2,2]
Output: [2]
Example 2
Input:  nums1 = [4,9,5],  nums2 = [9,4,9,8,4]
Output: [9, 4]
'''

'''
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
Example 1
Input:  nums = [3, 0, 1]    # n = 3, range [0,1,2,3]
Output: 2
Example 2
Input:  nums = [9,6,4,2,3,5,7,0,1]
Output: 8
'''