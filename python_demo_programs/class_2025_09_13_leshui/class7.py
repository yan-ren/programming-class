grades = {'Alice': [93, 90], 'Bob': [20, 10], 'Charlie': [50, 40]}

students = {'Alice': {'math': 90, 'english': 30},
            'Bob': {'french': 40, 'math': 49}}


'''
students = {"A001": "Tom", "A002": "Tom", "A003": "Anna"}

create: {"Tom": ["A001", "A002"], "Jerry": "A002", "Anna": "A003"}
'''
students = {"A001": "Tom", "A002": "Tom", "A003": "Anna"}

new_student = {}

for key, value in students.items():
    if value not in new_student:
        new_student[value] = [key]
    else:
        new_student[value].append(key)

print(new_student)

