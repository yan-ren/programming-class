
seq = [1, 2, 3, 4, 5]
[(x, x**2, x**3) for x in seq]

seq = [3, 8, 9, 5]
[True if i % 3 == 0 else False for i in seq]

# [expression for item in iterable if condition]
# [expression1 if condition else expression2 for item in iterable]
dic = {1 : 2, 3: 4}
# dic = {2:3, 4:5}