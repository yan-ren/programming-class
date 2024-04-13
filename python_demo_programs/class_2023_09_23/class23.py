# class Drawing:
#     def draw_square(self, symbol, size):
#         for row in range(size):
#             for col in range(size):
#                 print(symbol, end='')
#
#             print()
#
#     def draw_triangle(self, symbol, size):
#         for row in range(size):
#             for col in range(row+1):
#                 print(symbol, end='')
#
#             print()
#
#
# draw = Drawing()
# draw.draw_square('#', 4)
# draw.draw_triangle('#', 4)

class A:
    def __init__(self):
        self.x = 1
        self.y = 2

    def method_a(self):
        print('hello')

class B(A):
    def __init__(self):
        super().__init__()
        self.z = 3

    def method_b(self):
        print('welcome')


b = B()
print(b.x)
print(b.y)
print(b.z)
print(b.method_a())
print(b.method_b())

'''
Write a Python program to create a class that represents a shape. Include methods to calculate its area and perimeter, 
e.g, circle, triangle, and square
'''