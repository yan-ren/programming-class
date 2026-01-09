# for x in range(1, 100):
#     for y in range(1, 100):
#         print(x, y)

def sum_list(numbers):
    result = 0
    for num in numbers:
        result += num

    return result

def max_list(numbers):
    result = numbers[0]
    for num in numbers:
        if num > result:
            result = num

    return result

print(sum_list([1, 2, 3, 1, 2]))
print(sum_list([1, 1]))