'''
Class -> Object
We use object most of the time, sometimes we directly use class
Class: variable(static variable and instance variable) + method(static method and instance method)
'''

class Math:
    PI = 3.14 # class variable/static variable


class Student:
    # so constructor is also an instance method
    def __init__(self, id):
        self.id = id

    def speak(self):
        return self.id+"hello"
#
# Math.PI
#
s1 = Student(1)
print(s1.id) # object is the instance of class

# s1.id = 100
# print(s1.id)
# print(s1.speak()) # 100hello
#
# s2 = Student(2)
# print(s2.id)
# print(s2.speak()) # 2hello

'''
exercise
1. write a python class named Student with two instance variables student_id, student_name
2. add another instance variable called gender
3. create two objects from Student class, called student1 and student2
    for student1, use "Mark" as student_name, 1 as student_id, "m" as gender
    for student2, use "Grace" as student_name, 2 as student_id, "f" as gender
4. print student1's name and student2's id
5. change student1's name to "Tom", change student2's name to Lily

1. write a python class called Car, with two instance variable name and model
2. write a instance method called info which returns name + model
3. create an object called car1, with name = compact, model = toyota
4. call info method in car1
'''

'''
Write a python program to create a dictionary from a string
Given a string with all unique letters, the key of dictionary is the character in string,
where the value is the index of the character

s = "python"
d = {"p": 0, "y": 1, "t": 2, "h": 3, "o": 4, "n": 5}

s = "abc"
d = {"b": 1, "c": 2, "a": 0}
'''
# s = "abc"
# d = {ch:s.index(ch) for ch in s}

'''
exercise
1. Write a python class called Classroom, with a instance variable teacher
2. Write a python class called Teacher, with two instance variables, name and subject
3. write a python class called Student, with two instance variables, name and gender
'''

'''
write a python function that takes a string and returns a dictionary
the dictionary key is the each character in the string, the value is the frequency of the character

s = "abbc"
d = {"a": 1, "b": 2, "c": 1}

s = "hello"
d = {"h": 1, "e": 1, "l": 2, "o": 1}
'''