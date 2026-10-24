'''
check whether a list is sorted

Write is_sorted(numbers) that return True if the numbers are in nondecreasing order, equal values are allowed

e.g.
is_sorted([1, 3, 5, 10]) # True
is_sorted([1, 3, 15, 10]) # False

Hint: compare the first two elements then check the remaining list
'''
'''
base case: a list with zero or one element is already sorted
recursive step: if the first two are in the correct order, check the list starting from the second element
'''
def is_sorted(numbers):
    if len(numbers) < 1:
        return True

    if numbers[0] > numbers[1]:
        return False

    return is_sorted(numbers[1:])

'''
generate all permutations

write permutations(text) that returns a list containing every possible arrangement of the characters

assume all characters are distinct

e.g.

permutations('ab') # ['ab', 'ba']
permutations('a') # ['a']
permutations('abc') # ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

hint: choose each character as the first character, then recursively arrange the remaining characters

for 'abc'
first character  |     remaining characters    |    Permutations    |    Added to result    |
'a'                          'bc'                   'bc', 'cb'            'abc', 'acb'
'b'                          'ac'                                                                                                            '                   'ac', 'ca'            'bac', 'bca'
'c'                           'ab'                  'ab', 'ba'             'cab', 'cba'
'''

def permutations(text):
    if len(text) == 1:
        return [text]

    result = []
    for i in range(len(text)):
        first = text[i]
        remaining = text[:i] + text[i+1:]

        for perm in permutations(remaining):
            result.append(first + perm)

    return result

print(permutations('abc'))

'''
'ab'
pick 'a', remaining 'b' -> 'ab'
pick 'b', remaining 'a' -> 'ba'
'''