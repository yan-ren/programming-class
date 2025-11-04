# import sys
#
# lines = sys.stdin.read().strip().split()
# N = int(lines[0])
# arr = lines[1:] # list of 'P' or 'S'
#
# total_p = arr.count('P')
# if total_p == 0:
#     print(max(0, N-1))
#     sys.exit(0)
#
# # sliding window
# start = 0
# pcount = 0
# best = 0
#
# for end in range(N):
#     if arr[end] == 'P':
#         pcount += 1
#     while pcount > 1:
#         if arr[start] == 'P':
#             pcount -= 1
#         start += 1
#
#     best = max(best, end - start + 1)
#
# print(best)

numbers = [1, 2, -1, 4]
numbers.sort(reverse=True)
print(numbers)

new_numbers = sorted(numbers, reverse=True)
print(new_numbers)