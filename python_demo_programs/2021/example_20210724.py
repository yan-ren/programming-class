# Write a Python program to add two given lists and find the difference between lists.

# Original lists:
# [6, 5, 3, 9]
# [0, 1, 7, 7]

# Result:
# [(6, 6), (6, 4), (10, -4), (16, 2)]

# Write a Python program to split a given dictionary of lists into list of dictionaries using map function.
# Original dictionary of lists:
# {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}

# Split said dictionary of lists into list of dictionaries:
# [{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78}, {'Science': 62, 'Language': 84}, {'Science': 95, 'Language': 80}]

# m = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
# result = []
# for key, value in m.items():
#     tmp = []
#     for v in value:
#         tmp.append({key: v})
#     result.append(tmp)

# print(result)

# list1 = result[0]
# list2 = result[1]
# i = 0
# while i < len(list1):
#     list1[i].update(list2[i])
#     i += 1
# print(list1)

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self.age == other.age


p1 = Person('tim', 23)
print(p1)

p2 = Person('kim', 24)
print(p2)


print(p1 == p2)


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def rotate_90_CC(self):
        self.x, self.y = -self.y, self.x

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return "Point({0}, {1})".format(self.x, self.y)


p1 = Point(3, 4)
p2 = Point(2, 3)
p3 = p1 + p2
print(p3)
