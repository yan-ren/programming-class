'''
string
'''
s = "abc"
s = 'abc'

# zero or more characters in single or double quote
s = 'he said "hello"'
s = "he said it's 42"

greeting = 'hello'
group = 'world'
print(greeting + group) # concatenation

a = 1
b = 2
print(a + b)

a = '1'
b = '2'
print(a + b)

s = 'Arthur'
print(s[0])
print(s[1])
print(s[-5])
print(len(s))

# use while loop and index, loop through each character in string
index = 0
while index < len(s):
    print(s[index])
    index += 1


index = len(s) - 1
s_reverse = ''
while index >= 0:
    # print(s[index])
    s_reverse = s_reverse + s[index]
    index -= 1
print(s_reverse)

# given a string with letters, create a new string by removing all vowel
s = 'hello'
s_new = ''

i = 0
while i < len(s):
    if s[i] not in 'aeiou':
        s_new += s[i]
    i += 1

print(s_new)