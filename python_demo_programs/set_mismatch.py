# def find_error_numbers(nums):
#     mask = [0] * (len(nums)+1)
#
#     for i in nums:
#         mask[i] += 1
#
#     index = 1
#     while index < len(mask):
#         if mask[index] != 1:
#             print(index)
#         index += 1
#
#
# find_error_numbers([1, 2, 2, 4])

'''
Given a list of integers numbers from 1 to n, n is the length of the list
some numbers are repeated, find the number that repeats most

e.g.
l = [2, 2, 3, 3, 3, 4]
'''



# nums = [2, 2, 3, 3, 3, 4, 4, 4, 4, 4, 4]
# new = [0] * (len(nums)+1)
# for i in nums:
#     new[i] += 1
#
# print(new.index(max(new)))

'''
depth first search
- inorder traverse: left mid right
- preorder traverse: mid left right
8, 3, 1, 6, 4, 7, 10, 14, 13

- postorder traverse: left right mid
breath first search
'''

# l = [1] * 3
# print(l)
#
# def set_mismatch(l):
#     mask = [0] * (len(l) + 1)
#     for num in l:
#         mask[num] += 1
#
#     res = []
#     for num in mask:
#         if num != 1:
#             res.append(num)
#
#     return res
#
#
# set_mismatch([1, 2, 2, 4])

# l = [1,2,2,4]
# n = len(l)
# ans = []
# # add the duplicated number into the answer
# for i in range(1, n):
#     count = 0
#     for j in l:
#         if j == i:
#             count += 1
#     if count != 1:
#         ans.append(i)
#
# print(ans)

# text = input("enter text: ")
# print(text)
f = open('./resource.txt', 'w')
f.write("This is new line")
# line = f.readline()
#
# while line:
#     print(line)
#     line = f.readline()

