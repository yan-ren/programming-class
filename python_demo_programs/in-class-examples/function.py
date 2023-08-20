def talk(prompt, retries=4):
    print(prompt*retries)


# talk("hello")
# talk("hello")

def ask_yn(prompt, retries=4, compliaint="enter Y/N"):
    for i in range(retries):
        ok = input(prompt)
        if ok in ('Y', 'y'):
            return True
        if ok in ('N', 'n'):
            return False
        print(compliaint)
    return False


# ask_yn('hello', 1)
# ask_yn(prompt='hello', compliaint='world', retries=2)

# print('hello', end='')
# range(1, 10, step=2)
# argument vs parameter

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


# parrot(1000)
# parrot(voltage=1000) #keyword argument
# parrot(voltage=1000, action='vooom')
# parrot(action="voom", voltage=1000)
# parrot("a million", "bereft of life", "jump")
# parrot("a thousand", state="pushing up the daisies")
'''
parrot()

non-keyword argument cannot after a keyword argument
parrot(voltage=3.0, 'dead')

parrot(100, voltage=200)

parrot(actor='John')
'''

'''
Rules about function call
- keyword argument must follow non-keyword argument
- all keyword arguments must match with some parameter
- no paramter may receive a value more than once
'''


'''
Function scope


'''

# def f(a, b):
#     return b, a

# c, d = f(1, 2)


# t = (10, 20, 30, 40)

# a, *b, c = t
# print(a)
# print('type of b: ' + str(type(b)))
# print(b)

'''
Variadic positional arguments

A parameter of form *args capture exess positional args
The excess arguments are bundled into an args tuple

why do we use it?
call functions with any number of posiitonal arguments
'''

def product(*a, scale):
    # sum = 0
    # for i in a:
    #     sum += i
    
    return sum(a)*scale



# product(3, 5, scale = 6)
# product(3, 4, 2, scale=10)
# product(3, 5, scale=10)

l = [2, 3, 4, 5, 6]
print(product(*l, scale = 1))

def find_number(nums):
    return len([n for n in nums if len(str(n)) % 2==0])
