# def f1():
#     print('welcome')
#     print('Today is Monday')
#
# f1()
#
# def f2(numbers):
#     max = numbers[0]
#     min = numbers[0]
#
#     for value in numbers:
#         if value > max:
#             max = value
#         if value < min:
#             min = value
#
#     return min, max

# def f1():
#     print('hello')
#     f1()
#
# f1()

def f1(n):
    if n == 0:
        return
    print(n)
    f1(n-1)

f1(3)

# exercise: write a recursive function that prints from 1 to 10
