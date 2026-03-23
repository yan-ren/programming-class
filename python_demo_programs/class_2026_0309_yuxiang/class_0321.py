# numbers = [[1, 2, 1], [2, 3, 4], [1, 2, 3]]
#
# # how to generate a new list with largest number from each sub list
# # [2, 4, 3]
#
# result = []
#
# for sub in numbers:
#     # find largest for each sub
#     largest = sub[0]
#     for num in sub:
#         if num > largest:
#             largest = num
#
#     result.append(largest)
#
# print(result)
#
# numbers = [[1, -2, 1], [-2, 3, 4], [-1, -2, -3]]
# a = 1
# b = 1
# print(a)
# print(b)
#
# print(a, end='')
# print(b)

# def welcome():
#     print('welcome to the class')
#
# welcome()
# welcome()
#
# def calculation(a, b):
#     c = a + b
#     d = a - b
#     return c, d
#
# result1, result2 = calculation(1, 2)
# print(result1)

# def f1(a):
#     b = a + 1
#     return f2(b)
#
# def f2(a):
#     return a + 1
#
# print(f1(1))

# write a function taking a list as input and return the largest/smallest
def largest_smallest(numbers):
    largest = numbers[0]
    smallest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num

    return largest, smallest


print(largest_smallest([1, 2, 1, 2, 4]))
print(largest_smallest([1, 2, 3]))