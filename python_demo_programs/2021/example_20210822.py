'''
part 1, Student
1. write a class called student, which has instance varialbe student_name as string, grades as list
student_name initialize using value in constructor, grades initialized as empty list

2. write a method called add_grade, so we can append a number grade to the grades list

3. write a method called get_average, so that can get average grade from the grades list


part 2, Classroom
1. write a class called Classroom, which has instance variable classroom_id and a list of students, the list can be empty
2. write a method called add_student, which can add student to the list
    - only the student with at least one grade can be added
    - student_name cannot be empty
3. write a method called get_best_student that returns the student'name whose average grade is highest
'''


class Student:
    def __init__(self, name):
        self.student_name = name
        self.grades = []

    def add_grade(self, grade):
        if type(grade) == int:
            self.grades.append(grade)
        else:
            print('error: add_grade requires a number')

    def get_average(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades)/len(self.grades)

    def get_lowest_grade(self):
        if len(self.grades) == 0:
            return 0

        min = self.grades[0]
        for i in self.grades:
            if i < min:
                min = i

        return min


class Classroom:
    def __init__(self, id):
        self.classroom_id = id
        self.students = []

    def add_student(self, student):
        if student.student_name == '':
            return
        elif len(student.grades) == 0:
            return

        self.students.append(student)

    def get_best_student(self):
        best_student_name = ''
        highest_average = 0
        for student in self.students:
            if student.get_average() > highest_average:
                highest_average = student.get_average()
                best_student_name = student.name

        return best_student_name


student1 = Student('tom')
student1.add_grade(20)
student1.add_grade(30)
student1.add_grade(40)

print(student1.get_average())

student2 = Student('jerry')
student2.add_grade(48)
student2.add_grade(39)
student2.add_grade(32)

print(student2.get_average())

classroom = Classroom(1)
classroom.add_student(student1)
classroom.add_student(student2)
print(classroom.get_best_student())
