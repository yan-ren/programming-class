set = set()

set.add('hello')
set.add([1, 2])

# write a python function takes two list as input, check if one list contains another list
# [1, 2, 3] [1, 2] -> true
# [1] [1, 2, 3] -> true
# [1, 2] [1, 3] -> false

def contains(list1, list2):
    set1 = set(list1)
    set2 = set(list2)

    if len(set1 - set2) == 0 or len(set2 - set1) == 0:
        return True
    else:
        return False


def contains2(list1, list2):
    set1 = set(list1)
    set2 = set(list2)

    return set1 < set2 or set2 < set1


# homework:  Write a Python program to find maximum and the minimum value in a set.
# {1, 2, 3}