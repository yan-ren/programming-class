def example(a, b):
    return a + b, a - b

# res1, rest2 = example(1, 2)
# print(res1, rest2)
print(example(1, 2))

'''
function has scope, which defines the range of a function, also defines which variable stays
where.
'''
# x = 2 # global scope
# def foo(y):
#     z = 5
#     print(locals())
#     print(globals())
#     print(x, y, z)
#
# foo(3)

# x = 2
# def foo(y):
#     x = 41
#     z = 5
#     print(locals())
#     print(globals())
#     print(x, y, z)
#
# foo(3)

# if/loop has no scope
# success = True
# if success:
#     desc = 'winner'
# else:
#     desc = 'loser'
# print(desc)

# pass mutable / immutable variable to function
# mutable
# numbers = [1, 2, 3]
# numbers[1] = 3

# immutable
# s = 'abc'
# print(s[1])
# s[1] = 'd'

# numbers = [1, 2]
# print(numbers)
#
# def cal(num):
#     # num[0] += 1
#     num = [100, 100]
#     print(num)
#
# cal(numbers)
# print(numbers)

a = 1
def cal(b):
    b += 1
    print(b)

cal(a)
print(a)
