'''
s = 'YazaAay'


loop through the string, check if it has a letter that not have both upper case and lower case
if so, split the string and check for the left part and right part if they are valid, return the longer one

'YzazAay'

left = 'Y' 
right = 'azAzy'

for ch in s:



'''

def longest_nice_string(s):
    if len(s) < 2:
        return ''
    i = 0
    for ch in s:
        if ch.lower() not in s or ch.upper() not in s:
            left = s[:i]
            right = s[i+1:]
            left_result = longest_nice_string(left)
            right_result = longest_nice_string(right)
            if len(left_result) > len(right_result):
                return left_result
            else:
                return right_result
        i += 1
    return s

print(longest_nice_string('YazaAay'))