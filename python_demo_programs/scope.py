# x = 2
#
#
# def foo(y):
#     x = 41
#     z = 5
#     print(locals())
#     print(globals()['x'])
#     print(x, y, z)
#
# foo(3)
# print(x)

# This function uses global variable s
# def f():
#     print(s)
#
#
# s = "I love Geeksforgeeks"
# f()
# print(s)

# def f():
#     global s
#     print(s)
#     s = "That's clear."
#     print(s)
#
#
# s = "Python is great!"
# f()
# print(s)


def calculation():
    global place
    place = "Cape Town"
    global name
    name = "John"

    print("place in global:", 'place' in globals())
    print("place in local :", 'place' in locals())
    print("name in global :", 'name' in globals())
    print("name in local  :", 'name' in locals())
    return


place = "Berlin"
print(place)
calculation()
