from pygame_examples.car import MyClass
from pygame_examples.grade import Grade

# static variable can be accessed by class name
print(MyClass.num)

# create an object from MyClass
my_obj = MyClass(1)
my_obj1 = MyClass(2)
print(my_obj.name)
print(my_obj1.name)

my_obj.print('Steven')

# write a class with any name
# inside your class create two instance variables, called a and b
# the value for a and b is passed in through
# write an instance method call sum, which returns the sum of a and b
# try to use your class by creating object and call sum function

math_grade = Grade([])
math_grade.add_grade(1)
math_grade.add_grade(2)

english_grade = Grade([])
english_grade.add_grade(3)
english_grade.add_grade(4)

# create a new object from Grade class,
# which contains the combined values from math_grade and english_grade
combined = []
combined.extend(math_grade.grade_list)
combined.extend(english_grade.grade_list)
new_obj = Grade(combined)
