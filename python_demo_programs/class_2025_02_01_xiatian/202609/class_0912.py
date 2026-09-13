'''
class - OOP (Object-Oriented Programming)

class
object

def
'''
class Student:
    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = []

    def print_name(self):
        print('Student name', self.name)

    def get_average(self):
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        return 'Student name: ' + self.name

class Teacher:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.subject = None

class Classroom:
    def __init__(self):
        self.students = []
        self.teachers = []

    def highest_average_grades_students(self):
        best_students = []
        highest_grade = 0
        for student in self.students:
            if student.get_average() > highest_grade:
                best_students.clear()
                best_students.append(student)
                highest_grade = student.get_average()
            elif student.get_average == highest_grade:
                best_students.append(student)
        return best_students


s1 = Student('Alice', 12)
s1.print_name()
s1.grades.append(90)
s1.grades.append(91)
s1.grades.append(80)

s2 = Student('Bob', 19)
s2.print_name()
s2.grades.append(85)
s2.grades.append(86)

t1 = Teacher('Claire', 20)
classroom = Classroom()
classroom.students.append(s1)
classroom.students.append(s2)
classroom.teachers.append(t1)

print(s1.name)
print(s1)