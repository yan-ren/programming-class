class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x+other.x, self.y+other.y)


point = Point(1, 1)
point2 = Point(1, 1)
point3 = point + point2
print(point3.x)
print(point3.y)

'''
Write a Python program to combine two dictionaries adding values for common keys.
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}

{'a': 400, 'b': 400, 'd': 400, 'c': 300}

'''


def combine_dictionary(dic1, dic2):
    for key, value in dic1.items():
        if key in dic2:
            dic2[key] = dic1[key] + dic2[key]
        else:
            dic2[key] = value
    return dic2


d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}
print(combine_dictionary(d1, d2))
