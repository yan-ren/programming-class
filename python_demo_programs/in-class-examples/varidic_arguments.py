'''
variadic positional arguments

*args
excess arguments are bundled into an args tuple
'''

# for each value in nums, sum them and multiply by scale


def product(*nums, scale=1):
    s = 0
    for n in nums: # loop
        s += n
    
    return s*scale


# pass arguments without keyword
# positional arguments need to be include in the proper position or order
# product(3)
# product(3, 5)
# product(3, 4, 2)
# product(3, 5, scale=10)
# product(3, 5, 10, 10, 2, scale=10)


'''
varidic keyword arguments

** arguments
capture all excess keyword arguments
'''
def authorize(qoute, **info):
    print(qoute)
    print(info)
    for k, v in info.items():
        pass  


# authorize("hello", player=1, speaker=2, act=3)
# authorize("hello", player=1)
#
# d = {"author": 1, "player": 2}
# authorize("hello", **d)
'''
**d -> author=1, player=2
'''

'''
formatting string
'''

# s = 'first, count to {0} {0} {1}'.format(3, 4)
# print(s)


# n = 234
# product = 1
# sum = 0
#
# for i in str(n):
#     product *= int(i)
#     sum += int(i)


'''
list
tuple
dictionary
set
'''

# def get_numbers():
#     a = 1
#     b = 2
#     return a, b

# a, b = get_numbers()
# print(type(res))


# t = 1, 2, 3, 4, 5
# print(type(t))
# for i in t:
#     print(i)

# print(t[0])
# t[0] = 1

# a = 1
# b = 2

'''
right side we create a tuple (b, a)
left side we unpack the tuple into variables a and b
'''
# a, b = b, a


# t = (1, 2, 3, 4)
# a, *b, c = t
# print(a)
# print(b)
# print(c)
# print(type(b))

'''
parameter vs argument
'''

def test(a, b):
    print(a, b)

# c = 1
# test(c, 2)

'''
default parameter
'''
def test(a, b=1):
    print(a, b)

# test(a=1)
# test(b=2, a=1) # keyword argument


def parrot(voltage, state='a stiff', action='voom', type='blue'):
    print(voltage, state, action, type)

'''
positional argument
parrot(1000)

1 keyword argument
parrot(voltage=1000)


parrot(voltage=1000, action='boom')

parrot(action='boom', voltage=1000)

parrot('million', 'life', 'jump')

parrot('thousand', state='push')

parrot()

parrot('dead', voltage=100)
parrot('dead', voltage=100)

parrot(actor=100)
'''



# print(1, 2, sep=',')

'''
variadic arguments
* variadic positional arguments
** variadic keyword arguments
'''
# a, b are parameters
# def test(*a, b, c):
#     for n in a:
#         print(n)
#
#     print(a, b)
#
# # 1, 2 are arguments
# test(1, b=2, c=3)
# test(1, 2, b=3, c=2)

# def test(a, **b):
#     print(a)
#     print(b)
#
# test(1, keyword1=1, keyword2=2, keyword3=3)
# def test(*a, **b):
#     print(a)
#     print(b)
#
# test(1, 2, k1=3, k2=4)
'''
q1: is this a correct function, meaning can I run this function without error?
q2: if it's correct, how to call the function
'''
'''
formatting strings
'''
# s = 'First you can count to {0} {0} then {1} and {2}'.format(1, 2, 3)
# print(s)
# s = 'first you can count to {number}'.format(number=1)
# print(s)
# s = "{0}{b}{1}{a}{0}{2}".format(5, 8, 9, a='z', b='x')
'''
(5, 8, 9)
{a='z', b='x'}
'''
# print(s)
'''
a, b are mandatory positional arguments
c optional keyword argument
d variadic positional arguments
e optional keyword argument
f variadic keyword argument
'''
def foo(a, b, c=1, *d, e=1, **f):
    pass

'''
first class functions: a programming languages treats functions as first-class citizens
first-class citizen:
- supports passing functions as arguments to other functions
- supports returning function as value from other functions
- assign function to variable

python functions are objects, python supports first-class functions
which means in python, functions can be passed as arguments to other function, 
returned as the values from other functions and assigned to variables
'''
# def echo(arg):
#     print(arg)
#
#
# # a = echo
# # a(1)
# # print(type(a))
#
# def greet(f):
#     f("hello")
#
# greet(echo)

'''
* variadic positional arguments
** variadic keyword arguments
'''
def product(*nums, scale):
    print(nums)
    print(scale)


def authorize(quote, **speaker_info):
    print(quote)
    print(speaker_info)


def testing(*args, **kwargs):
    print(args)
    print(kwargs)


# test(1, 2, 3, a=1, b=2, c=2)
# product(1, 2, 3, scale=1)
# authorize(1, a=1, b=2)
'''
string formatting
'''
'''
format(*args, **kwargs)
'''
# {n} refers to the n-indexed positional argument
# s = 'First, you count {2}{2}'.format(1, 2, 3)
# print(s)

# s = "throw your {0}".format(1, 2, 3, 4, weapon=1, tool=2)

s = "{0}{b}{1}{a}{0}{2}".format(5, 8, 9, a='z', b='x')
'''
args=(5, 8, 9)
kwargs={a='z', b='x'}
'''
'''
first-class function
- function can be passed as arguments to other function
- returned as the values from other functions
- assigned to variables
'''
# function assigned to variable



# yell = shout
# print(yell('hello'))

'''
function passed as arguments to other functions
'''
# def shout(text):
#     return text.upper()
#
#
# def whisper(text):
#     return text.lower()
#
#
# def greet(f):
#     print(f('hello'))
#
# a = 1
# a = whisper
#
# greet(shout)
# greet(whisper)

def create(x):
    def add(y):
        return x + y
    return add


def add(y):
    a = 1
    return a

a = create(5)
b = create(20)
'''
add(y):
    return 5 + y
'''

'''
write a function which takes a list of numbers as input
return a new list with only positive numbers

[1, 2, -1, -2]

[1, 2]
'''
# def only_positive(l):
#     for i in l:
#         if i <= 0:
#             l.remove(i)
#     return l
#
# lol = only_positive([1, -1, 2, -2])
# print(lol)

# l = [1, 2, 3, 3, 3]
# l.remove(1)
# print(l)
# l.remove(3)
# print(l)
#
#
# def only_positive(l):
#     res = []
#     for num in l:
#         if num > 0:
#             res.append(num)
#     return res
'''
prime number

A number can only be divided by 1 and itself

11 -> 1 and 11
2
3
5
7
11
13

check 7
2
3
4
5
6
'''
# def is_prime(number):
#     i = 2
#     while i < number:
#         if number % i == 0:
#             return False
#         i += 1
#
#     return True
#
# # covert to a program, e.g. ask user a number and tell if the number is prime or not
# value = int(input('Write a number: '))
# if is_prime(value):
#     print("Prime number")
# else:
#     print("Not prime")
'''
Example: safe input for integers

Goal:
write a function that repeatedly asks a user to enter an integer, 
until the number entered in within a desired range. Once a valid input has been entered,
return that value

'''

'''
Ask user to enter a value by printing message
repeat until value is between minVal and maxVal
'''
def input_in_range(message, min_value, max_value):
    while True:
        n = int(input(message))
        if min_value <= n <= max_value:
            return n
        else:
            print("number outside of range", min_value, max_value)


age = input_in_range("Enter age:", 0, 120)
height = input_in_range("Enter height in cm:", 0, 250)

'''
Goal:
write a function that repeatedly asks a user to enter a string, 
until the string entered in within a desired list of acceptable values. 
Once a valid input has been entered, return that value
'''
# def input_in_list(message, acceptable_list):
#     while True:
#         s = input(message)
#         if s in acceptable_list:
#             return s
#         else:
#             print("Please respond by ", acceptable_list)
#
#
# gender = input_in_list("what's your gender?", ['female', 'male'])
# history = input_in_list("history of covid?", ['yes', 'no'])
