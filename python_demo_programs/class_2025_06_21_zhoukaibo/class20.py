'''
2024 J3

solution:
1. put all numbers into list
2. create a new list without duplicated
3. sorted non-duplicated list, find the third largest
4. count number of third largest in original
'''
# numbers = [1, 2, 3, 1, 2, 4, 4]
#
# numbers.sort()
# print(numbers)
#
# new_numbers = sorted(numbers)
# print(numbers)

'''
given a list of number find the third largest value
1. create a new list without duplicates
2. sort and find the third largest value, third position from the right
'''
numbers = [1, 2, 1, 2, 4, 4, 4, 3]

new_numbers = []
for num in numbers:
    if num not in new_numbers:
        new_numbers.append(num)

print(new_numbers)
new_numbers.sort()
print(new_numbers[len(new_numbers) - 3])

print(numbers.count(2))