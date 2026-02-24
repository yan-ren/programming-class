fruits = ['apple', 'banana', 'apple', 'orange', 'pear']

# find which fruits showed up the most
# two solution
# 1. without dictionary
most_frequent = 0
most_frequent_fruit = ''

for fruit in fruits:
    count = fruits.count(fruit)
    if count > most_frequent:
        most_frequent = count
        most_frequent_fruit = fruit

print(most_frequent_fruit)

# 2. with dictionary

# create a dictionary the key is fruit, value is count, loop through the list
# increase the count by one each time
'''
{
'apple': 2, 'banana': 1, 'orange': 1, 'pear': 1
}
'''
counter = {}
for fruit in fruits:
    if fruit not in counter:
        counter[fruit] = 1
    else:
        counter[fruit] += 1

print(counter)

most_frequent = 0
most_frequent_fruit = ''

for fruit, count in counter:
    if count > most_frequent:
        most_frequent = count
        most_frequent_fruit = fruit

print(most_frequent_fruit)

grades = {'math': [90, 89, 29, 30, 90], 'english': [30, 21, 32, 45, 99], 'physics': [39, 21, 49, 20, 39]}
for subject, marks in grades.items():
    max, min = marks[0], marks[0]
    for m in marks:
        if m > max:
            max = m
        if m < min:
            min = m
    print('High', max, 'Low', min)
