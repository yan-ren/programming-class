def message():
    print('Hello')
    print('Welcome')


message()
message()

def say_hello(name):
    print('Hello', name)

say_hello('Bob')
# say_hello() # error


def add(a, b):
    return a + b

result = add(3, 4)

# write a function which takes a list as input, return the sum of all number in the list
def sum_list(l):
    s = 0
    for value in l:
        s += value

    return s

print(sum_list([1, 2, 3, 4]))

# Write a function count_vowels(text) that returns the number of vowels in the string.
# e.g. count_vowels("hello")  # Expected: 2

# s = 'hello'
# for letter in s:
#     if letter in 'aeiou':
#

# Write a function reverse_string(s) that returns the reversed string.
# reverse_string("python")  # Expected: "nohtyp"
def reverse_string(s):
    s_new = ''

    for letter in s:
        s_new = letter + s_new

    return s_new

