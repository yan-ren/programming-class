# numbers = [1, 2, 1, -3, -4]
#
# def count_positive(nums):
#     count = 0
#     for num in numbers:
#         if num > 0:
#             count += 1
#
#     return count
#
# print(count_positive(numbers))
#
# # return the sum of all positive values from the list
# # def sum_positive(nums):
#
# # write a function which takes two lists as input and return a combined list
# # input: [1, 2] [2, 3]
# # return:[1, 2, 2, 3]
# def merge(list1, list2):
#     combine = []
#
#     # loop list1 and append each value to combine
#     for v in list1:
#         combine.append(v)
#
#     # same for list2
#     for v in list2:
#         combine.append(v)
#
#     return combine
#
#
# print(merge([1, 3], [1, 2]))


# import turtle
#
# shape = input("Enter 'triangle' or 'square': ").strip().lower()
#
# turtle.speed(3)
#
# def draw_square():
#     for _ in range(4):
#         turtle.forward(100)
#         turtle.left(90)
#
# def draw_triangle():
#     for _ in range(3):
#         turtle.forward(100)
#         turtle.left(120)
#
# if shape == "triangle":
#     draw_triangle()
# elif shape == "square":
#     draw_square()
# else:
#     print("Invalid input. Please enter 'triangle' or 'square'.")
#
# turtle.done()

# Write a function that takes a list and returns a new list containing
# only unique elements (remove duplicates).
def unique(l):
    new_l = []

    for v in l:
        if v not in new_l:
            new_l.append(v)

    return new_l








