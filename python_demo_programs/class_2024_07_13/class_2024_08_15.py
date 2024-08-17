'''
8/4/2024
Write a function which takes two sorted list, return a single list
which is merged by two input list and the returned list is also sorted

list1 = [1, 2, 4, 5, 7]
list2 = [2, 3, 6, 10, 11]

returned = [1, 2, 2, 3, 4, 5, 6, 7, 10, 11]
'''


def merge_two_sorted_list(list1, list2):
    res = []

    i = 0
    j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            res.append(list1[i])
            i += 1
        else:
            res.append(list2[j])
            j += 1

    while i < len(list1):
        res.append(list1[i])
        i += 1

    while j < len(list2):
        res.append(list2[j])
        j += 1

    return res


print(merge_two_sorted_list([1, 2, 4, 5, 7], [2, 3, 6, 10, 11]))

'''exercise 2024/08/15
https://leetcode.com/problems/longest-common-prefix/description/
'''