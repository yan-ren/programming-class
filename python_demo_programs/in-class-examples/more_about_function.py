'''
oop: object oriented programming
'''

'''
default/named parameter
'''
# from socket import VM_SOCKETS_INVALID_VERSION


def ask(message, repeat=4, complaint='nothing'):
    print(message * repeat)
    print(complaint)



'''
parameter vs argument
'''
'''
keyword argument
'''
h = "hello"
ask(h, 1)
ask(repeat=3, message='hello') 

# call with only the mandatory argument
# ask('done?')

# call with one keyword argument
# ask('done?', repeat=3)

# # call with one keyword argument in any order
# ask('done?', complaint='N/A')

# # call with all of the keyword arguments
# ask('done?', complaint='n/a', repeat=1)

# def parrot(voltage, state='stiff', action='voom', type='blue'):
#     print(voltage, state, action, type)


# parrot(1000)
# parrot(voltage=1000)
# parrot(voltage=100, action='voom')
# parrot(action='voom', voltage=100)
# parrot('a million', 'bereft of life', 'jump')

'''
parrot()
parrot(voltage=4, 'dead')
parrot('dead', voltage=4)
parrot(actor='john')
'''

'''
rules about function calls
- keyword argument must follow positional arguments/non-keyword argument
- all keyword arguments must identify some parameter
- positional argument also identify some parameter
- no parameter may receive a value more than once
'''

'''
homework:
subtract the product and sum of digits of an integer

general:
work for all programming language
'''

from math import prod


def subtract_and_product_1(num):
    sum = 0
    mul = 1

    while num > 0:
        # module gives the right most digit
        sum += num % 10
        mul *= num % 10

        # divide by ten removes the right most digit
        num = num // 10
    
    return mul - sum

print(subtract_and_product_1(234))

def subtract_and_product_2(num):
    product = 1
    sum = 0

    for i in str(num):
        sum += int(i)
        product *= int(i)

    return product - sum

def find_diff_prodsum(num):
    new = [int(i) for i in str(num)]
    sum_of = sum(new)
    product = math.prod(new)
    return product - sum_of


def test():
    return 'abc', 123, 321

# res = test()
# print(type(res))
# a, b = res
# print(a, b)

# *a, b = test()
# print(type(a))
# print(a)
# print(type(b))
# print(b)

# a, *b, c = (1, 2, 3, 4, 5)

'''
variadic positional arguments

a parameter with * captures the excess positional arguments

why?
call functions with any number of inputs
'''
def product(*nums, scale=1):
    print(nums)
    print(scale)


# product(3, scale=4)
product(3, 4)
# product(3, 4, scale=5)

'''
variadic keyword arguments

a parameter with ** capture all excess keyword arguments
'''

# each keyword arguemtn is packed together as a dictionary
def authorize(quote, **info):
    print(quote)
    print(info)
    for k, v in info.items():
        print(k, v)

d = {"player":1, "act":1, "speaker":2}
authorize("hello", **d) # dictionary unpacking, each pair is passed into function




