# s = 'abcde'
# index = 0
# while index < len(s):
#     print(s[index])
#     index += 1
#
# # loop through charaters in string using for loop
# # string is iterable, it can be used in for loop
# # in each iteration, one character will be assigned to the variable ch
# for ch in s:
#     print(ch)

'''
list: a data structure, data structure is used to better organize the data in program
if you need three values in your program, how are you going to do it
'''
# a = 1
# b = 2
# c = 3

# list1 = []
# print(list1)
# list1.append(1)
# print(list1)
# list1.append(10)
# print(list1)
#
# for n in list1:
#     print(n)
#
# # loop through the list using while loop
# # hint: same thing as string, list also has index
# index = 0
# while index < len(list1):
#     print(list1[index])
#     index += 1
#
# list1.append('string')
# print(list1)
#
# list1.remove(10)
# print(list1)
# print(list1[0])

# l = [1, 3, 1, 2, 4, 5]
# # how to calculate the sum of all numbers in the list
# sum = 0
# for i in l:
#     sum += i
#
# print(sum)
#
# sum = 0
# index = 0
# while index < len(l):
#     sum += l[index]
#     index += 1


# def count_negative(matrix):
#     row = 0
#     column = len(matrix[0]) - 1
#     negative_count = 0
#
#     while row < len(matrix) and column >= 0:
#         if matrix[row][column] < 0:
#             negative_count += len(matrix[0]) - row
#             column -= 1
#         else:
#             row += 1
#
#     return negative_count

'''
p = PriorityQueue()
p.add(key, value)
p.remove_min()

p.add(5, 'A')
p.add(3, 'B')
p.remove_min()
'''


class PriorityQueue:

    class Item:
        def __init__(self, k, v):
            self.key = k
            self.value = v

    def __init__(self):
        self.store = []

    def __len__(self):
        return len(self.store)

    def add(self, key, value):
        e = self.Item(key, value)
        self.store.append(e)

    def remove_min(self):
        min_index = 0
        min_key = self.store[0].key
        i = 0
        while i < len(self.store):
            if self.store[i].key < min_key:
                min_key = self.store[i].key
                min_index = i
            i += 1

        min_value = self.store[min_index].num
        del self.store[min_index]
        return min_value


p = PriorityQueue()
p.add(5, 'A')
p.add(3, 'B')
p.remove_min()
print(len(p))


def countNegatives(grid):
    count = 0
    for g in grid:
        for g2 in g:
            if g2 < 0:
                count += 1

    return count

def count_negative(grid):
    row = 0
    column = len(grid[0]) - 1
    count = 0

    while row < len(grid) and column >= 0:
        if grid[row][column] > 0:
            row += 1
        else:
            count += len(grid) - row
            column -= 1

    return count

print(count_negative([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))
