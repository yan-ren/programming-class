class Student:
    def __init__(self, id, age):
        self.id = id
        self.age = age
        self.subjects = []

    def add_subject(self, subject):
        # check this subject name, only if the subject is
        # french, english, math, science
        if subject.name in ['english', 'french', 'math', 'science']:
            self.subjects.append(subject)

    # find and return the subject with the highest grade
    def get_best_subject(self):
        highest = -1
        name = None
        for s in self.subjects:
            if s.grade > highest:
                name = s.name

        return name

    def get_avg_grade(self):
        sum = 0
        for s in self.subjects:
            sum += s.grade

        return sum / len(self.subjects)

    # write a method to check which subject is missing
    # return a list of string with missing subject name

class Subject:
    def __init__(self, name):
        self.name = name
        self.grade = 0


s1 = Student(1, 10)
s1.add_subject(Subject('math'))
print(s1.subjects[0].name)
print(s1.get_best_subject())
# s1.id

# m = Subject('math')
# s1.add_subject(m)