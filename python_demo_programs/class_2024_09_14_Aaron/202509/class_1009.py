'''
Todo:
1. Windows laptop setup Github
2. Unreal project design idea, a written proposal about what do you want to build
'''
# when writing a function if need to return two value, what do we do
# e.g. how to write a function that takes a list of number and return min and max

def find_min_max(numbers):
    min = numbers[0]
    max = numbers[0]
    for value in numbers:
        if min > value:
            min = value
        elif value > max:
            max = value

    return min, max

# a, b = find_min_max([1, 2, -1, 4])
matrix = [[1, 2, 4, -2], [1, 2, 4, 2], [2, 5, 3, 0]]

# write a function find all min max from a matrix
# e.g. [[-2, 4], [1, 4], [0, 5]]
def find_all(m):
    # m is a 2d list, loop each sub list, call find_min_max function to get min, max
    # put min, max in to a result list
    result = []
    for sub in m:
        min, max = find_min_max(sub)
        result.append([min, max])

    return result

find_all([[-2, 4], [1, 4], [0, 5]])

# dictionary: key-value pair
# car = {'toyota': {'country': 'JP', 'year': 2020, 'color': 'red'}}
# # how to add another brand to above dictionary
# car['honda'] = {'country': 'JP', 'year': 2021, 'color': 'black'}
# print(car)
#
# for k, v in car.items():
#     v['year'] += 1

# print(car)

# how to put above code into a function
def increase_year(car_dic):
    for k, v in car_dic.items():
        v['year'] += 1

    return car_dic

car = {'toyota': {'country': 'JP', 'year': 2020, 'color': 'red'}}
print(increase_year(car))
