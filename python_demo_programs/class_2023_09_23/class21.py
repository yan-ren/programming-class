l = [1, 2, 3]
print(l.count(2))


class Car():
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def start_engine(self):
        print(self.brand + " starts")

    def stop_engine(self):
        print('engine stops')


car1 = Car('toyota', 1998)
# print(car1.brand)
#
# # class: blueprint of object, which define how each object should look like
# # object: object is created from class, it's the specific instance of class
# car2 = Car('mazda')
# car3 = Car('honda')



class GradeCalculator:
    def __init__(self, subject):
        self.grades = []
        self.subject = subject

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_average(self):
        return sum(self.grades) / len(self.grades)


calculator = GradeCalculator('math')
calculator.add_grade(20)
calculator.add_grade(30)
print(calculator.grades)
print(calculator.get_average())

calculator2 = GradeCalculator('science')
calculator2.add_grade(30)
calculator2.add_grade(30)
print(calculator2.get_average())

'''
1. create a Student class that stores each student info, e.g. name, age, grade
2. create a Classroom class, which has a list to store multiple student object created in step1.
    - write a function in Classroom to return the oldest student
    - write a function in Classroom to return the youngest student
    - option: write a function to return the student name start with a given letter
'''