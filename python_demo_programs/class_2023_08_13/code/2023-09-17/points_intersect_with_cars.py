first = {1, 2, 3}
second = {3, 4, 5}

# set operation
# set union
# third = first.union(second)
third = first | second
print(third)

# intersection
# third = first.intersection(second)
third = first & second
print(third)

# difference
# the difference betwen two sets is the set of all the elements in first set
# that are not presetn in the second set
first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}

print(first.difference(second))
print(second.difference(first))

# first - second

# symmetric difference
# The symmetric difference between two sets is the set of all the elements 
# that are etiher in the first set or the second set but not in both
first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}

first.symmetric_difference(second)
second.symmetric_difference(first)
first ^ second


def numberOfPoints(nums):
    s = set()
    for start, end in nums:
        s = s | set(range(start, end + 1))

    return len(s)