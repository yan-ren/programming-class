'''
find duplicated letters from a string

write a python function which takes a string as input, return the list of letters that are duplicated in string

e.g.
input: aabcddeeffff
output: ['a', 'd', 'e', 'f']
'''

def find_duplicated_letters(str):
    res = []
    for ascii in range(97, 123):
        # print(chr(ascii))
        count = 0
        for letter in str:
            if letter == chr(ascii):
                count += 1

        if count > 1:
            res.append(chr(ascii))

    return res


print(find_duplicated_letters('aabcddeeffff'))
print(find_duplicated_letters('abcdecae'))
