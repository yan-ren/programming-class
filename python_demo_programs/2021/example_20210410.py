# student_name1 = "Jacky"
# student_gender1 = "male"
# student_email1 = "xxx@gmail.com"

class Student:
    id = 1 # class variable/static variable
    def __init__(self, name, age): # constructor, it is called when an object is created from the class
        self.name = name # object variable/instance variable
        # self.age = age
        pass

    def set_name(self, name):
        self.name = name

# print(Student.id)

student1 = Student("Tom", 12)
print(student1.name)
student1.set_name("Jerry")
print(student1.name)

# student2 = Student("Jerry", 13)
# print(student2.name)
# print(student2.age)
'''
reverse integer
Given an integer x, return x with its digits reversed.
e.g. x = 123
return 321

x = 120
return 21

x = -32
return -23
'''
# def reverse_string(input):
#     input = str(input)
#     input = input[::-1]
#     return int(input)
#
# print(reverse_string(123))
# print(reverse_string(210))

num = 1234
num = num*-1
num = str(num)
num = num[::-1]
num = int(num)
num = num*-1
print(num)
print(type(num))