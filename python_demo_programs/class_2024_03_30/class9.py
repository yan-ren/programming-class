'''
merge function
'''
def find_max(list):
    max = list[0]
    for value in list:
        if value > max:
            max = value

    return max


def merge(list1, list2):
    if len(list1) == 0 and len(list2) == 0:
        return

    res = []
    for value in list1:
        res.append(value)
    for value in list2:
        res.append(value)

    # find the max value and return the max
    max = find_max(res)
    return max


result = merge([1, 2, 3], [2, 3, 4])
print(result)

'''
exercise: write a function which takes a list of numbers, return the list with only non-duplicated numbers
receive: [1, 2, 1, 4, 2, 5]
return: [1, 2, 4, 5]
'''
# def deduplicate(list):
#     res = []
#     for value in list:
#         if value not in res:
#             res.append(value)
#
#     return res

'''
exercise: write a function which takes a list of numbers, 
there is one repeated number, find the repeated number
given [1, 2, 3, 1, 4, 5]
return 1
'''

d = {}
d['first_name'] = 'Tom'
d['last_name'] = 'Smith'

print(d)
print(d['first_name'])
d['first_name'] = 'Jerry'
print(d)

numbers = [1, 2, 1, 4, 2, 5, 6]
count = {}

for num in numbers:
    if num in count:
        count[num] = count[num] + 1
    else:
        count[num] = 1

print(count)