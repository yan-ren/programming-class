# class Person:
#     # class variable/static variable
#     nationality = "canadian"
#     # instance variable
#     # constructor/megic method

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def print_name(self):
#         print(self.name)


# class Student(Person):


# print(Person.nationality)

# p = Person("tom", 21)
# print(p.name)
# print(p.age)
# p.print_name()

# 1. create a class called _marks that has a instance variable called "_marks" which is a empty list
# 2. write a method called add_mark that adds int value to "_marks" instance variable
# 3. write a method called get_highest that return the highest mark from "_marks"
# 4. write a method called get_average that return the average mark from "_marks"
# 5. add another instance variable called names which is a list


# class Marks:
#     def __init__(self):
#         self._marks = []
#         self.names = []

#     def add_mark(self, name, mark):
#         self._marks.append(mark)
#         self.names.append(name)

#     def get_highest(self):
#         if len(self._marks) == 0:
#             return None
#         result = self._marks[0]
#         index = 0
#         while index < len(self._marks):
#             if result > self._marks[index]:
#                 result = self._marks[index]
#                 name = self.names[index]
#             index += 1
#         return result, name

#     def get_average(self):
#         if len(self._marks) == 0:
#             return None
#         return sum(self._marks) / len(self._marks)


# math_marks = Marks()
# math_marks.add_mark("tom", 39)
# print(math_marks._marks)

'''
Given an list nums containing n distinct numbers in the range [0, n], 
return the only number in the range that is missing from the array.

Input: nums = [3,0,1] n=3  [0,3]
Output: 2

Input: nums = [9,6,4,2,3,5,7,0,1] n=9 -> [0,9]
Output: 8
'''


def missing_number(l):
    l.sort()
    i = 0
    while i <= len(l):
        if i not in l:
            return i
        i += 1


'''
given a list of string in email format
['yan@gmail.com', 'yan@hotmail.com', 'yan@live.com', 'tom@gmail.com']

create a dictionary where the key the is user name, value is the list of emails for the user
{'yan':['yan@gmail.com', 'yan@hotmail.com', 'yan@live.com'], 'tom': ['tom@gmail.com']}

hint:
string.split
'''
# email = "yan@gmail.com"
# result = email.split("@")
# print(result)


def process_people_emails(l):
    people_dic = {}
    for email in l:
        user_name = email.split("@")[0]
        if user_name in people_dic:
            people_dic[user_name].append(email)
        else:
            people_dic[user_name] = [email]

    return people_dic
