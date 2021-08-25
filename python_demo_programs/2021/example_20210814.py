
# def search(list, target):
#     for i in list:
#         if i == target:
#             return True
#     return False


# def binary_search(list, target):
#     left = 0
#     right = len(list) - 1

#     while left <= right:
#         mid = (left + right) / 2
#         if list[mid] > target:
#             right = mid - 1
#         elif list[mid] < target:
#             left = mid + 1
#         else:
#             return True

#     return False


def bubble_sort_1(list):
    number_of_values = len(list)
    i = 0
    while i < number_of_values-1:
        index = 0
        while index < number_of_values-1:
            if list[index] > list[index+1]:
                tmp = list[index]
                list[index] = list[index+1]
                list[index+1] = tmp
            index += 1
        i += 1
    return list


def bubble_sort_2(list):
    number_of_values = len(list)
    i = 0
    sorted = False
    while not sorted:
        index = 0
        sorted = True
        while index < number_of_values-1:
            if list[index] > list[index+1]:
                tmp = list[index]
                list[index] = list[index+1]
                list[index+1] = tmp
                sorted = False
            index += 1
        i += 1
    return list


def selection_sort(list):
    # loop through each position of the list
    for i in range(len(list)):
        # find the min element in remaining
        min_index = i
        for j in range(i+1, len(list)):
            if list[min_index] > list[j]:
                min_index = j
        # swap i with min_index
        list[i], list[min_index] = list[min_index], list[i]

    return list


list = [6, 5, 4, 3, 2, 1]
print(bubble_sort_1(list))
