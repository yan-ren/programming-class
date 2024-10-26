'''exercise
Given a list of strings, find the longest string from the list
Given: ['abc', 'a', 'bc', 'abdec']
output: 'abdec'
'''
words = ['abc', 'a', 'bc', 'abdec', 'aaaaaaa']
longest_str = words[0]

for w in words:
    if len(w) > len(longest_str):
        longest_str = w

print(longest_str)