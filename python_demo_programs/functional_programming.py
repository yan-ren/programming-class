'''
Programming Paradigms
OOP: Object Oriented Programming
FP: Functional Programming

why use functional programming
- avoid objects by providing small independent functions
- pass existing function to other functions for new task

map/filter
'''

# a common problem
'''
input = [1, 2, 3, 4]
output = []

def f(n):
    return -n

for element in input:
    val = f(element)
    output.append(val)

print(output)

[f(element) for element in input]
'''

'''
map(fn, iterable)

'''
'''
input = [1, 2, 3, 4]

def f(n):
    return -n


l = list(map(f, input))
print(l)
''' ,

languages = ['python', 'perl', 'java']
l = list(map(len, languages))
print(l)

'''
input = [1, 2, -1, 3]
output = [1, 2, 1, 3]

lambdas expression
'''
input = [1, 2, -1, -3]
s = map(abs, input)
print(type(s))
print(s)
