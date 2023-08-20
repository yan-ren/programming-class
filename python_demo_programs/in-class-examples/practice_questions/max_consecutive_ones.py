# given = [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1]
# if given[-1] == 1:
#     given.append(0)
#
# counts = []
# x = 0
# for i in given:
#     if i == 1:
#         x += 1
#     else:
#         counts.append(x)
#         x = 0
#
# print(max(counts))
#
#
# nums = [1, 0, 1, 1, 1]
# count = 0
# maximum = 0
# m = len(nums)
#
# for i in range(0, m):
#     if nums[i] == 1:
#         count += 1
#         if count > maximum:
#             maximum = count
#     if nums[i] == 0:
#         count = 0
# print(maximum)

'''
[1, 0, 1, 1]
'''

# def find_max_consecutive_ones(nums):
#     max_count = 0
#     count = 0
#     for num in nums:
#         if num == 1:
#             count += 1
#         elif count > max_count:
#             max_count = count
#             count = 0
#     if count > max_count:
#         max_count = count
#     return max_count
#
#
# def cons_1(n):
#     answers = []
#     count = 0
#     array = n.split()
#     ar = []
#     for i in array:
#         ar.append(int(i))
#     for j in ar:
#         if j == 1:
#             count += 1
#         elif j == 0:
#             answers.append(count)
#             count = 0
#
#     return max(answers)
#
# n = input("Please numbers (1 or 0):")
# print(cons_1(n))

# def findMaxConsecutiveOnes(nums):
#     str_nums = ''.join([str(i) for i in nums])
#     largest_len = 0
#     for i in str_nums.split('0'):
#         if len(i) > largest_len:
#             largest_len = len(i)
#
#     return largest_len
#
# nums = [1, 0, 1, 1, 0, 1]
# print(findMaxConsecutiveOnes(nums))
#
#
def max_consective_ones(nums):
    counter = 0
    max_count = 0
    for n in nums:
        if n == 1:
            counter += 1
        elif max_count < counter:
            max_count = counter
            counter = 0

    if counter > max_count:
        max_count = counter

    return max_count


print(max_consective_ones([1, 1, 0, 1, 1, 1]))


def max_consecutive_ones(nums):
    top = 0
    count = 0

    for n in nums:
        if n == 1:
            count += 1
        else:
            count = 0

        if count > top:
            top = count

    return top

