'''
variadic argument
positional variadic argument *args
keyword variadic argument
'''
def product(*nums):
    print(type(nums))
    print(nums)

# passing positional arguments
# product(1, 2)
# product(1, 2, 3)
def authorize(**speak):
    print(type(speak))
    print(speak)


authorize(act=1, name='li', age=2)
authorize(act=1, age=2)

def test(*args, **kwargs):
    print(args)
    print(kwargs)

test(1, 2, a=1)

'''
string.format(*args, **kwargs)
'''
s = 'first this is {0} {1} {a}'
# print(s.format(3, 1, 2, 3, a=1, b=2))
print("{0}{b}{1}{a}{0}{2}".format(5, 8, 9, a='z', b='x'))
