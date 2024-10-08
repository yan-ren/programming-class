def two_sum(nums, target):
    # range(4)
    '''
    i = 0
    while i < len(nums):

    '''
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return i, j

    return -1, -1


nums = [2, 7, 11, 15]
print(two_sum(nums, 9))
print(two_sum([3, 2, 4], 6))
print(two_sum([3, 3], 6))
# len(nums) -> 4

'''
Homework:
Write a Python function that takes a single string as input and returns True if the string is a palindrome and False otherwise.

A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward

Example1:
s = 'madam'

return True
'''

# e.g. text = 'madam'
def is_palindrome(text):
    i = 0
    j = len(text) - 1
    while i < j:
        if text[i] != text[j]:
            return False
        i += 1
        j -= 1

    return True

print(is_palindrome('madam'))

'''
More thing to think about it:

123321 -> '123321'
'''

number = 123321
s = str(number)
