'''
why function
'''
# def message():
#     print('Welcome to the game!')
#     print('Today is Wednesday!')
#
#
# def message2(name):
#     print('Hello, ' + name)
#     print('Welcome, ' + name)
#
# message2('Chanel')
# message2('Wendy')
#
# def message3(name, age):
#     print('Hello, ' + name)
#     print('Welcome, ' + name)
#     print('Age is ' + str(age))
#
# message3('Wendy', 19)
#
# def school(a, b, c):
#     d = a + b + c
#     return d
#
# result = school(5, 6, 7)
# print(result)

'''
given a list of numbers, find the largest
'''

numbers = [1, 2, 6, 3, 4]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num

print(largest)

def find_largest(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num

    return largest

print(find_largest([1, 2, 6, 3, 4]))
print(find_largest([10, 2, 60, 30, 4]))

s = 'hello'

'''
Write a function named find_string(x, y), The first parameter x is guaranteed to be a list containing
only string values. The second parameter y is a string. The function returns the index of the leftmost element on x
that matches y. If no element on x matches y, the function must return -1. The function must not change the list x!

for example, if the function is called as follows:
ls = ['red', 'yellow', 'blue', 'green', 'blue']
y = find_string(ls, 'blue')
z = find_string(ls, 'violet')

y is 2
z is -1
'''

'''
logic: check each value in the list one by one to find a match, as long as finding a match return immediately.
if all checks are done and not return, meaning not matching we need to return -1
'''
def find_string(x, y):
    i = 0
    while i < len(x):
        if x[i] == y:
            return i # exit function
        i += 1

    return -1

print(find_string(['red', 'yellow', 'blue', 'green', 'blue'], 'blue'))

'''
variation: x is a list of strings, y is a string, find how many y exists in x
'''
def count_matches(x, y):
    count = 0
    for s in x:
        if s == y:
            count += 1

    return count

print(count_matches(['red', 'yellow', 'blue', 'green', 'blue'], 'blue'))
