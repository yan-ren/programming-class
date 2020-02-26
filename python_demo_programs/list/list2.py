"""
Google Classroom list Q5

Give a list of string, count how many items of list has length longer than 3
"""
a = ['aaa', 'abc', 'ab', 'abcdef', 'abcde']
index = 0
counter = 0

while index < len(a):
    if len(a[index]) > 3:
        counter += 1
    index += 1
print(counter)