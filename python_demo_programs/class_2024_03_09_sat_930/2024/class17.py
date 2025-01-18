'''
Write a function that takes two lists of numbers as inputs and compares the average of the numbers in each list.
The function should return a string indicating which list has a higher average, or if the averages are equal.
'''


def compare_average():
    avg1 = sum(list1) / len(list1)
    avg2 = sum(list2) / len(list2)

    if avg1 > avg2:
        return 'list 1 has a higher average'
    elif avg2 > avg1:
        return 'list 2 has a higher average'
    else:
        return 'both lists have equal average'


list1 = [1, 2]
list2 = [2, 3]

res = compare_average()
print(res)

print(compare_average())

'''
Write a function that takes two lists of numbers as inputs and returns a new list containing the element-wise sum of the two input lists.

list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(element_wise_sum(list1, list2))  # Output: [5, 7, 9]
'''
def element_wise_sum(list1, list2):
    result = []

    index = 0
    while index < len(list1):
        result.append(list1[index] + list2[index])
        index += 1

    return result

'''homework
Write a function that takes two lists of numbers as inputs and returns a new list containing the element-wise sum of the two input lists.

list1 = [1, 2, 3]
list2 = [4, 5, 6, 7]
print(element_wise_sum(list1, list2))  # Output: [5, 7, 9, 7]
'''