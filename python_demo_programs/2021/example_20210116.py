# fn(x) = x
# fn(x) = x ** 2
# def fn(x):
#     return x ** 2
#
#
# a = [fn(x) for x in range(10)]

# l1 = [1, 2, 3, 4]
# l2 = [x if x % 2 == 0 else x + 1 for x in l1]
# print(l2)

# l = []
# for i in range(5):
#     for j in range(i):
#         l.append((i, j))

# fruits = ['apple', 'mango', 'banana', 'cherry']
# a = {f: len(f) for f in fruits}
# print(a)
# a = {f:f.upper() for f in fruits}
# print(a)
#
# fruits = {'apple': 1, 'mango': 2, 'banana': 3, 'cherry': 4}
# remove = {'apple', 'cherry'}
# {key:fruits[key] for key in fruits.keys() - remove}