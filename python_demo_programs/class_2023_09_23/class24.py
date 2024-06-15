def linear_search(numbers, target):
    for value in numbers:
        if value == target:
            return True
    return False

def binary_search(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left <= right:
        mid = (left + right) // 2
        # check if target is at mid
        if numbers[mid] == target:
            return True
        elif numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False


numbers = [2, 1, 4, 5, 3]
target = 3
print(linear_search(numbers, target))
numbers.sort()
print(binary_search(numbers, target))

def bubble_sort(list):
    for i in range(len(list)):
        index = 0
        swap = False
        while index < len(list) - 1:
            if list[index] > list[index + 1]:
                # swap the value
                tmp = list[index]
                list[index] = list[index + 1]
                list[index + 1] = tmp
                swap = True
            index = index + 1

        if not swap:
            return list

    return list


numbers = [1, 2, 5, 4, 3]
numbers = bubble_sort(numbers)
print(numbers)
