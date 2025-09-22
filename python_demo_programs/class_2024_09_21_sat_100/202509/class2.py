grades = {
    "Alice": [30, 20, 40],
    "Bob": [12, 30, 25],
    "Chris": [23, 40, 20]
}

'''
create a new dictionary contains the average grade for each person
avg = {
    "Alice": 30,
    ...
}
'''
def get_avg(grades):
    avg = sum(grades) / len(grades)
    return avg

avg = {}

for name, grade in grades.items():
    avg[name] = round(get_avg(grade), 2)

print(avg)