'''
write a function which takes a list as input and return the min and max value inside the list
'''

def min_max(list):
    max = list[0]
    min = list[0]
    for value in list:
        if value > max:
            max = value
        if value < min:
            min = value

    return max, min

print(min_max([1, 2, 3, 4, 5]))
