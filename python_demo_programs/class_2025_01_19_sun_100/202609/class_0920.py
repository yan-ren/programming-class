# squares = []
# for i in range(10):
#     squares.append(i**2)
# print(squares)
#
#
# squares = [i**2 for i in range(10)]
# print(squares)
#
# word = 'Abe'
# new_word = []
#
# for ch in word.lower():
#     if ch not in 'aeiou':
#         new_word.append(ch)
#

# number = []
# for i in range(5):
#     for j in range(i):
#         number.append((i, j))
#
# numbers = [0, 1, 2, 3]
# new_nubmers = [num * 2 + 1 for num in numbers]
# print(new_nubmers)
#
# numbers = [3, 8, 9, 5]
# result = [num % 3 == 0 for num in numbers]
# print(result)

fruits = ["apple", "banana", "cherry"]
result = [f[0].upper() for f in fruits]

result = [(f, len(f)) for f in fruits]

numbers = [1, 2, 3, 4]
result = ['even' if num % 2 == 0 else 'odd' for num in numbers]
result = ['positive' if num > 0 else 'negative' for num in numbers]
