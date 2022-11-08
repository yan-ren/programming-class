class Grade:
    def __init__(self, grade_list):
        self.grade_list = grade_list

    def add_grade(self, grade):
        self.grade_list.append(grade)
