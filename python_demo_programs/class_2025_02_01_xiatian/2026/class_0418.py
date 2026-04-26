# object oriented programming

# why do we need oop
# Enemy 1
enemy1_name = "Goblin"
enemy1_hp = 50
enemy1_x = 100
enemy1_y = 200

# Enemy 2
enemy2_name = "Skeleton"
enemy2_hp = 30
enemy2_x = 400
enemy2_y = 150

# class: put all related variable together
# class Dog:
#     # constructor
#     def __init__(self, name, breed, age):
#         self.name = name
#         self.breed = breed
#         self.age = age
#
# dog1 = Dog('Buddy', 'Golden', 3)
# print(dog1.name)
# print(dog1.breed)
# print(dog1.age)
# dog1.age += 1
# dog1.name = 'Buddy Buddy'
#
# dog2 = Dog("Luna", "Husky", 5)

# class Dog:
#     def __init__(self, name):
#         self.name = name
#         self.energy = 100
#
#     def bark(self):
#         print(self.name, 'Woof woof')
#
#     def fetch(self):
#         self.energy -= 10
#         print(self.name, 'fetches! Energy: ', self.energy)
#
#     def nap(self):
#         self.energy = min(100, self.energy + 30)
#         print(self.name, 'takes a nap. Energy', self.energy)
#
#
# dog = Dog('Buddy')
# dog.bark()
# dog.fetch()
# dog.nap()

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def avg(self):
        sum = 0
        for g in self.grades:
            sum += g

        return sum / len(self.grades)

s1 = Student('Bob')
s1.grades.append(50)
s1.grades.append(60)


class Classroom:
    def __init__(self):
        self.students = []

c1 = Classroom()
c1.students.append(s1)
