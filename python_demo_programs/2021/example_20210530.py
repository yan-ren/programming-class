'''
Write a Python program of recursion list sum
e.g. [1, 2, [3,4], [5, [6, 7]]]
return 21

base case: when element is single value, just add to the sum
recursive case: when element is a list, call function get the sum of the list
'''
# def recursive_sum(l):
#     res = 0
#     for i in l:
#         if isinstance(i, int):
#             res += i
#         else:
#             res += recursive_sum(i)
#     return res
#
# # write a class named Person, with firstname and lastname instance variable and a printname method
#
# class Polygon:
#     def __int__(self, no_of_sides):
#         self.n = no_of_sides
#
#     def print_sides(self):
#         print(self.n)
#
#
# class Triangle(Polygon):
#     def __init__(self, color):
#         super().__int__(self, 3)
#         self.color = color
#
#
#
# triangle = Triangle("red")
# print(triangle.color)
# print(triangle.n)
# print(triangle.print_sides())
#
# class Person:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#
#     def print_name(self):
#         print(self.first_name, self.last_name)
#
#
# class Student(Person):
#     def __init__(self, id, first_name, last_name):
#         super().__init__(self, first_name, last_name)
#         self.id = id


'''
Write a Python program to calculate the sum of the positive integers of n+(n-2)+(n-4)... (until n-x =< 0).
Test Data:
sum_series(6) -> 6 + 4 + 2 + 0 = 12
sum_series(10) -> 10 + 8 + 6+ 4+ 2+ 0 = 30 
'''

'''
write a non-recursive function that calculate the nth fibonacci number
'''
def fib(n):
    fib_1 = 0
    fib_2 = 1
    if n == 1:
        return fib_1
    elif n == 2:
        return fib_2

    i = 2
    result = 0
    while i < n:
        result = fib_1 + fib_2
        fib_1 = fib_2
        fib_2 = result
        i += 1
    return result

print(fib(5))
print(fib(8))

def fib_recursive(n):
    # base case
    if n == 1:
        return 0
    elif n == 2:
        return 1
    # recursive case
    return fib_recursive(n-1) + fib_recursive(n-2)

'''
Write a Python program of recursion list sum
e.g. [1, 2, [3, 4], [5, [6, 7]]]
return 21

base case: when element is single value, just add to the sum
recursive case: when element is a list, call function get the sum of the list
'''
def sum_all(list):
    result = 0
    for i in list:
        if type(i) == int:
            result += i
        else:
            result += sum_all(i)

    return result


print(sum_all([1, 2, [3,4], [5, 6]]))
