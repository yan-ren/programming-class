'''
2025 J3

string traversal
string indexing
string slicing

# given a string, how to use while loop to loop through each letter

# s = 'abc'
# for ch in s:
#     print(ch)
#
# i = 0
# while i < len(s):
#     print(s[i])
#     i += 1
#
# print(s[i:j])

'''

N = int(input())

def process(s):
    i = 0
    letters = ''
    value = 0

    while i < len(s):
        if 'A' <= s[i] <= 'Z':
            letters += s[i]
            i += 1
        elif '0' <= s[i] <= '9' or s[i] == '-':
            j = i + 1
            while j < len(s) and s[j].isdigit():
                j += 1
            value += int(s[i:j])
            i = j # update index i
        else:
            i += 1
    return letters + str(value)


for i in range(N):
    s = input()
    print(process(s))

'''
given a string, with letters, only keep the vowels

e.g. 
input: 'aaaeqidklj'
output: 'aaaei'
'''
s = 'aaaeqidklj'
i = 0
result = ''
while i < len(s):
    if s[i] in 'aeiou':
        result += s[i]
    i += 1

print(result)

for ch in s:
    print(ch)