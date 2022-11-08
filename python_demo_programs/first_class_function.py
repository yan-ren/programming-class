'''
first class function
- functions can be passed as arguments to other functions
- functions can be returned as the values from other functions
- functions can be assigned to variable

object

in python functions are objects
'''
def shout(text):
    return text.upper()
#
# def greet(f):
#     print(f('hello'))
#
#
# greet(shout)
yell = shout
# print(yell('word'))
# print(shout('hello'))

def create(x):
    def adder(y):
        return x+y

    return adder

# a = create(4)
# print(a(1))
'''
a = def adder(y):
        return 4+y
'''
f = open('text.txt')
for line in f:
    print(line, end='')

f.close()


with open('text.txt', 'w') as f:
    # context = f.read()
    # print(context)
    f.write("we are writing to the file")

'''
pure functions: 
'''
class Name():
    def __init__(self):
        self.x = 1

'''
add :: Integer, Integer -> Integer
'''
def f(x):
    return x+1

# output = []
# for element in [1, 2, 3, 4]:
#     val = f(element)
#     output.append(val)

# [f(element) for element in [1, 2, 3, 4]]


s = map(lambda val: val**2, [1, 2, 3, 4])
print(type(s))
print(list(s))
