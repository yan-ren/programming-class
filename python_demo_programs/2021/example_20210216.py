x = 2  # value 2 is in an object
print(isinstance(2, object))
print(id(400))
print(id(400))
print(id(400))
print(id(400))
print(id(400))
# generally speaking, the id of object is assigned at runtime,
# not same between each run
print(id(4))

x = 2000
y = "hello"
print(locals())

x = 1
y = 1.0
# == compares the value of two object
# 1 and 1.0 they are considered as the same
print(x == y)
print(x is y)


# homework
# you can solve it using anything you learned so far
# find the median
# write a method to find the median from a list of numbers
# median is the middle number in a sorted list of numbers
# [2, 3, 4, 1] -> [1, 2, 3, 4] median = 2
# [2, 1, 4] -> [1, 2, 4] median = 2
# if list has odd number of values, middle value is the median
# if list has even number of values, median is the average of middle pair, e.g. 2.5 in above example

def median(l):
    l.sort()
    if len(l) % 2 == 0:
        return (l[len(l) // 2] + l[len(l) // 2 - 1]) / 2
    else:
        return l[len(l) // 2]

print(median([2, 3, 4, 1]))