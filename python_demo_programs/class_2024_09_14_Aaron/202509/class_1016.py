'''
Mix data structure

list
dictionary
set
tuple
'''

'''
1. How do you create a list of dictionaries, and how can you add a new dictionary to that list?
'''
cars = [
    {'brand': 'toyota', 'year': 2022, 'color': 'red'},
    {'brand': 'honda', 'year': 2023, 'color': 'black'},
    {'brand': 'toyota', 'year': 2019, 'color': 'white'}
]

# ask user for their car brand, year, color, create a new dictionary and put it in the list

'''
2. Given a list of dictionaries, how can you search for a dictionary where a certain key equals a specific value?
'''

# how to get all toyota from the cars list, loop through each car dictionary and check their brand
for car in cars:
    if car['brand'] == 'toyota':
        print(car)

'''
Write a function that takes a list of dictionaries and a key name, 
and returns a new list containing the values for that key from each dictionary.

input:
cars = [
    {'brand': 'toyota', 'year': 2022, 'color': 'red'},
    {'brand': 'honda', 'year': 2023, 'color': 'black'},
    {'brand': 'toyota', 'year': 2019, 'color': 'white'}
]
'toyota'

return
[{'year': 2022, 'color': 'red'}, {'year': 2019, 'color': 'white'}]
'''
def extract(cars, key):
    result = []
    for car in cars:
        if car['brand'] == key:
            result.append({'year': car['year'], 'brand': car['brand']})

    return result

