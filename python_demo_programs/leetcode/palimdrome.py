'''
Write a function that takes a string as input and determines whether it is a palindrome or not. 
A palindrome is a word, phrase, number, or other sequence of characters that reads the same forwards and backwards, 
ignoring spaces, punctuation, and letter casing.

new requirment: using recursion to solve this problem

Input:
A string s of length n (1 ≤ n ≤ 10^5)

Output:
Return a boolean value indicating whether the input string is a palindrome or not.



nun

kayak

old solution:
1. using loops, and compare
2. 

new solution:
1. using recursion?

'''

s = 'abcd'
print(s[ : :-1])
'''
1. using slicing to slice the string from right to left
2. compare the original string with sliced string
'''
'''
base case:
if string is empty or only has one character?


recursive case:

'''
def is_palindrome(s):
    # base case
    if len(s) <= 1:
        return True
    
    # recursive case
    # compare the first and last character
    if s[0] == s[len(s) - 1]:
        # continue to compare the rest of the string by removing the first and last characters
        return is_palindrome(s[1:len(s)-1])
    else:
        return False


input_str = input('Enter a string:')
if is_palindrome(input_str):
    print('The string is a palindrome')
else:
    print('This string is not a palindrome')