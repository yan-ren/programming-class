# N = int(input())
#
# days = []
# for _ in range(N):
#     days.append(input())

# import sys
#
# lines = sys.stdin.read().strip().split() # ['8', 'P', 'S', 'P, 'S', 'S', 'P', 'P, 'S' ]
# N = int(lines[0])
# days = lines[1:]
#
# if days.count('P') == 0:
#     print(N-1)
#     sys.exit(0)
#
# left = 0
# p_count = 0
# longest = 0
#
# for right in range(N):
#     if days[right] == 'P':
#         p_count += 1
#
#     while p_count > 1:
#         if days[left] == 'P':
#             p_count -= 1
#         left += 1
#
#     # if right - left + 1 > longest:
#     #     longest = right - left + 1
#     longest = max(longest, right - left + 1)
#
# print(longest)

# numbers = [1, 2, -1, 6]
# numbers.sort(reverse=True)
# print(numbers)
#
# new_numbers = sorted(numbers, reverse=True)
# print(new_numbers)

N = int(input())
numbers = []
for _ in range(N):
    numbers.append(int(input()))

unique = []
for num in numbers:
    if num not in unique:
        unique.append(num)

unique.sort()

third = unique[-3]

print(third, numbers.count(third))