def method1():
    print(1)

method1()

class MyClass:
    num = 12345

    def greet(self):
        return "hello world"


class Student:
    def __init__(self, name):
        # create an object variable called "name"
        self.name = name

    def greet(self):
        return "welcome"


student1 = Student("Jacky")
print(student1.name)
# my_object = MyClass()
# print(my_object.num)
# print(my_object.greet())
#
# my_object_2 = MyClass()
# print(my_object_2.num)
# student1 = Student()
# print(student1.greet('Tom'))
'''
Merge Sorted List
Given two sorted integer lists nums1 and nums2, merge nums2 into nums1 as one sorted list

example
Input: nums1 = [1,2,3], nums2 = [2,5,6]
Output: [1,2,2,3,5,6]
'''
nums1 = [1,2,3]
nums2 = [2,5,6]
res = []
i = 0
j = 0

while i < len(nums1) and j < len(nums2):
    if nums1[i] < nums2[j]:
        res.append(nums1[i])
        i+=1
    else:
        res.append(nums2[j])
        j+=1

while i < len(nums1):
    res.append(nums1[i])
    i += 1

while j < len(nums2):
    res.append(nums2[j])
    j += 1

'''
Reverse Integer
Given an integer x, return x with its digits reversed

e.g. 
x = 12345
return 54321

x = 200
return 2
'''