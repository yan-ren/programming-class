'''
J3: loop/if else/list
J4: data structure:
1. list
2. dictionary
comprehension

3. set
4. tuple*
better to have: def

recursion

2025 J4
find the longest continues S with one chance to convert P to S
'''
# N = int(input())
#
# days = []
#
# for _ in range(N):
#     days.append(input())
import sys

# lines = sys.stdin.read().strip().split() # ['8', 'P', 'S', 'P', 'S', 'S', 'P', 'P', 'S']
# N = int(lines[0])
# days = lines[1:]
#
# if days.count('P') == 0:
#     print(N-1)
#     sys.exit(0)
#
# left = 0
# longest = 0
# p_count = 0
#
# for right in range(N):
#     if days[right] == 'P':
#         p_count += 1
#     while p_count > 1:
#         if days[left] == 'P':
#             p_count -= 1
#         left += 1
#
#     longest = max(longest, right - left + 1)
#
# print(longest)
