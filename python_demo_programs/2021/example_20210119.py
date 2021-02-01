# x = 1
# x = x + 1
# # shortcut
# x += 1

# squares = []
# for x in range(10):
#     squares.append(x**2)

# def power(x):
#     return (x + 1) * 3 ** 2
#
#
# squares = [power(x) for x in range(10)]
# print(squares)

# list = []
# numbers = [1, 2, 3, 4, 5]
# for i in numbers:
#     if i % 2 == 0:
#         list.append(i)
#
# l = [i for i in numbers if i % 2 == 0]
# print(l)

# convert following comprehension into normal code
# sentence = ['hello', 'WORLD']
# l = [word.lower() for word in sentence]
#
# word = 'hello'
# l = [ch for ch in word.lower() if ch not in 'aeiou']
#
# l = []
# for ch in word.lower():
#     if ch not in 'aeiou':
#         l.append(ch)
#
# print(l)

# seq = [1, 2, 3, 4]
# l = [(x, x**2, x**3) for x in seq]
#
# l = []
# for x in seq:
#     l.append((x, x**2, x**3))
# print(l)

# [0, 1, 2, 3] -> [1, 3, 5, 7]
numbers = [0, 1, 2, 3]
l = [i*2+1 for i in numbers]

# [3, 8, 9, 5] -> [True, False, True, False]
