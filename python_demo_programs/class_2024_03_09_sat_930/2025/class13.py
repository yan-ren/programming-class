numbers = [2, 1, 4, 3, 5]
numbers.sort()
print(numbers)

# sorting algorithm

'''
- CS
- Project
    - Python
        - game
        - AI application
    - React
'''

def bubble_sort(list):
    n = len(list)
    for i in range(n):
        sorted = True
        # last i elements are already sorted
        for j in range(n-1):
            if list[j] > list[j+1]:
                # swap list[j] with list[j+1]
                tmp = list[j]
                list[j] = list[j+1]
                list[j+1] = tmp
                sorted = False
        if sorted:
            break

    return list

my_list = [64, 34, 25, 12, 22, 11, 90]
my_list_sorted = bubble_sort(my_list)
print(my_list_sorted)