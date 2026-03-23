'''
list
set
dictionary
tuple
'''
'''
Problem
You are given a list of integers nums and an integer target. 
Return True if any two different elements in the list add up to target, otherwise return False.

example1
Input:  nums = [2, 7, 11, 15],  target = 9
Output: True
Explanation: 2 + 7 = 9

example2
Input:  nums = [1, 4, 6, 8],  target = 3
Output: False
Explanation: No two numbers add up to 3

def two_sum(nums, target):
    seen = {}
    for num in nums:
        # What are you looking for?
        complement = target - num
        
        # Is it in your dictionary?
        if complement in seen:
            return True
        
        # Store current number in dictionary
        seen[num] = True
    
    return False
'''


def two_sum(nums, target):
    seen = {}
    for num in nums:
        # What are you looking for?
        complement = target - num

        # Is it in your dictionary?
        if complement in seen:
            return True

        # Store current number in dictionary
        seen[num] = True

    return False

print(two_sum([2, 7, 11, 15], 9))

'''
Given a list of integers nums, return the element that appears most frequently. 
If there is a tie, return the smallest of the tied elements.

Input:  nums = [1, 3, 3, 2, 1, 3]
Output: 3
Explanation: 3 appears 3 times, more than any other element

Input:  nums = [4, 4, 6, 6, 2]
Output: 4
Explanation: 4 and 6 both appear twice — return the smallest, which is 4

def most_frequent(nums):
    counts = {}
    
    # Step 1: Count each element
    for num in nums:
        if num in counts:
            counts[num] = counts[num] + 1
        else:
            counts[num] = 1
    
    # Step 2: Find the highest count
    best = nums[0]
    for num in counts:
        if counts[num] > counts[best]:
            best = num
        elif counts[num] == counts[best] and num < best:
            best = num
    
    return best
'''
'''
You are given two lists of strings list1 and list2. 
Return a list of all words that appear in one list but not the other (in any order).

example1
Input:  list1 = ["apple", "banana", "cherry"]
         list2 = ["banana", "cherry", "date"]
Output: ["apple", "date"]
Explanation: "apple" is only in list1, "date" is only in list2

example2
Input:  list1 = ["cat", "dog"]
         list2 = ["cat", "dog"]
Output: []
Explanation: All words appear in both lists

'''