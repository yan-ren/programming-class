grades = {
    "Alice": [85, 90, 78],
    "Bob": [92, 88, 95],
    "Charlie": [70, 65, 72],
    "Diana": [88, 79, 85]
}

# Write a program to calculate the average score for each student and store it in a new dictionary.
# Example output:
# {'Alice': 84.33, 'Bob': 91.67, 'Charlie': 69.0, 'Diana': 84.0}

avg_grades = {}

# if we don't use sum, create a function to calculate the sum of a list
def cal_sum(numbers):
    s = 0
    for num in numbers:
        s += num
    return s

for name, grades in grades.items():
    # calculate the avg from grades and put it into the avg_grades
    avg_grades[name] = sum(grades) / len(grades)

print(avg_grades)

class Student:
    def __init__(self):
        self.name = ''
        self.age = 0
        self.grade = 10
# object = class
s1 = Student()
s2 = Student()

s1.name = 'Alice'
s2.name = 'Bob'

s1.age = 10
s2.age = 12

print(s1.grade)
print(s2.grade)

s1.grade = 11
print(s1.grade)
print(s2.grade)

# write a class represents a car
class Car:
    def __init__(self):
        self.color = ''
        self.brand = ''
        self.year = ''

'''
Given a list of pairs [[1, 2], [3, 2], [4, 5]] find which pair has the largest sum
'''