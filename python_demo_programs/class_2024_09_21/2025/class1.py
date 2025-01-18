# D = int(input())
#
# while True:
#     Y = int(input())
#
#     if D > Y:
#         D += Y
#     else:
#         print(D)
#         break

# N = int(input())
# distinct_numbers = []
# original_numbers = []
#
# for i in range(N):
#     num = int(input())
#     original_numbers.append(num)
#     if num not in distinct_numbers:
#         distinct_numbers.append(num)
#
#
# # use sorting to find the third-largest value
# # then count how many times this value exists in the original numbers
# distinct_numbers.sort()
# bronze_score = distinct_numbers[len(distinct_numbers) - 3]
# bronze_count = original_numbers.count(bronze_score)
# print(bronze_score, bronze_count)

numbers = [2, 1, 3, 4, 2, 5, 1]
print(min(numbers))
print(max(numbers))
# if 30 in numbers:
#     print(numbers.index(30))
# while 2 in numbers:
#     numbers.remove(2)
# print(numbers)

# a = [1, 2, 3]
# b = [2, 4, 1]
# a.extend(b)
# print(a)
# print(b)

# exercise: 2023 j2, j3