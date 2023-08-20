
# global scope
# x = 2

# def foo(y):
#     z = 5 # local scope
#     print(locals())
#     print(globals()['x'])
#     print(x, y, z)

# foo(3)
# print(z)

'''
when searching for a variable: function scope -> enclosing function scope -> global scope -> builtins -> error
'''

# x = 2

# def foo(y):
#     x = 41
#     z = 5 # local scope
#     print(locals())
#     # print(globals()['x'])
#     print(x, y, z)
#     if xxx:
#         x

# foo(3)

# def my_func():
#     x = 300
#     def my_another_func():
#         print(x)
#     my_another_func()

# my_func()

# x = 300

# def my_func():
#     x = 200
#     print(x)

# my_func()
# print(x)

# global keyword
# use the global keyword, can define a variable belongs to the global scope
x = 200
def my_func():
    global x
    x = 300

my_func()
print(x)