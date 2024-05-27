
# l = [2, 3, 4, 1, 6, 6]

# s = 0
# for value in l:
#     s += value
#
# print(s)

# print(sum(l))
# print(l.count(6))

# target = 6
# counter = 0
# for value in l:
#     if value == target:
#         counter += 1
#
# print(counter)

l = [-2, -3, -4, -1, -6, -6]
# print(max(l))
max_value = l[0]
for value in l:
    if value > max_value:
        max_value = value

print(max_value)