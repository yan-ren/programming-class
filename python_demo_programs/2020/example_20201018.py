# homework
# write a python function takes two lists as input, check if one list contains another list
# [1, 2, 3] [1, 2] -> true
# [1] [1, 2, 3] -> true
# [1, 2] [1, 3] -> false


def contain(list1, list2):
    # loop through list1 check if each element in list1 is also in list2
    list2_contains_list1 = True
    for i in list1:
        if i not in list2:
            list2_contains_list1 = False

    # loop through list2 check if each element in list2 is also in list1
    list1_contains_list2 = True
    for i in list2:
        if i not in list1:
            list1_contains_list2 = False

    return list1_contains_list2 or list2_contains_list1

# print(contains([1, 2, 3], [1, 2]))
# print(contains([1], [1, 2, 3]))
# print(contains([1, 2], [1, 3]))

# l = [[1, 2], 3]
# print(1 in l)
# print([1, 2] in l)

# write a python function that takes a list and a int, check if list contains two values that sum is the input int
# case1 [1, 2, 3], 4 -> True
# case2 [1, 2, 3], 10 -> False
# case3 [1, 3, 5], 4 -> True
# case4 [4, 2, 1], 5 ->

def pair_sum(list, sum):
    i = 0
    while i < len(list):
        j = i + 1
        while j < len(list):
            if list[i] + list[j] == sum:
                return True
            j += 1
        i += 1

    return False

# write a python function that takes a list and a int, check if list contains two values that diff is the input int
