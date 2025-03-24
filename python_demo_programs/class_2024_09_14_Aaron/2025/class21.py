'''
Count Vowels:
Write a function count_vowels(s) that counts and returns the number of vowels in the given string.
'''
def count_vowels(s):
    count = 0
    for ch in s:
        if ch in 'aeiou':
            count += 1

    return count

'''
Palindrome Check: 
Write a function is_palindrome(s) that checks if a given string s is a palindrome.
'''
def is_palindrome(s):
    # create a reversed string
    s_reversed = ''
    for ch in s:
        s_reversed = ch + s_reversed


print(is_palindrome('aba'))
print(is_palindrome('abc'))

def function_a():
    print("Function A is calling Function B")
    function_b()

def function_b():
    print("Function B is calling Function C")
    function_c()

def function_c():
    print("Function C is calling Function D")
    function_d()
    print('Function C is done')

def function_d():
    print("Function D has been reached!")

# Start the function chain
function_a()


def greet(name='Guest'):
    print(f"Hello, {name}!")

greet()
greet("John")

def calculate(a, b):
    sum_ = a + b
    diff = a - b
    return sum_, diff

s, d = calculate(10, 5)
print(s)