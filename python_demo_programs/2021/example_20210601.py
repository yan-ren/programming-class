'''
Write a Python program to calculate the sum of the positive integers of n+(n-2)+(n-4)... (until n-x =< 0).

n = 8
8 + 6 + 4 + 2 + 0

n = 8
f(8) = 8 + f(6)
f(6) = 6 + f(4)
f(4) = 4 + f(2)
f(2) = 2 + f(0)
f(0) = 0


f(n) = n + f(n-2)
f(n-2) = n-2 + f(n-4)
f(n-4) = n-4 + f(n-6)



9 + 7 + 5 + 3 + 1
'''

def f(n):
    if n <= 0:
        return 0
    return n + f(n-2)

print(f(8))
# def recursive_sum(n):
#     sum = 0
#
#     if n < 0:
#         return sum
#     else:
#         sum += n
#         sum += recursive_sum(n - 2)
#         return sum
#
#
# def recursive_sum(n):
#     if n < 0:
#         return 0
#
#     return n + recursive_sum(n-2)
#
# '''
# n! = n * (n-1) * (n-2) * (n-3) * ... * 1
# '''

class MyClass:
    num = 12345

    def greet(self, msg):
        return "Hello world!" + msg

# create an object called "x" using MyClass blueprint
x = MyClass()
print(x.greet(" welcome"))

'''
class is the blueprint of the object, to use the class, we need to create object from the class
'''

'''
Given a string, count total number of consonants in it. 
A consonant is a English alphabet character that is not vowel (a, e, i, o and u). 
Examples of constants are b, c, d, f, g, ..

input: abcde
return 3

how to solve it using non-recursive and recursive solution
'''
'''
s = "absent"

s = "a" + "bsent"

"bsent" = "b" + "sent"


'''


def nonVolwelCountRecursive(string):
    if len(string) == 0:
        return 0

    if string[0] in ['a','e','i','o','u']:
        return 0 + nonVolwelCountRecursive(string[1:])

    return 1 + nonVolwelCountRecursive(string[1:])

print(nonVolwelCountRecursive("absent"))


def nonVowelCount(string):
    count = 0

    for letter in string:
        if letter.lower() not in ['a', 'e', 'i', 'o', 'u']:
            count += 1

    return count

'''
encapsulation
abstraction
inheritance
polymorphism
'''


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def print_person(self):
        print(self.first_name, self.last_name)


# Student class inherits Person class, Person class is the base class of Student
class Student(Person):
    def __init__(self, student_id, first_name, last_name):
        super().__init__(self, first_name, last_name)
        self.student_id = student_id

    def print_student(self):
        print(self.student_id, self.first_name, self.last_name)


'''
kayak -> palindrome

write a recursive function check if a string is palindrome or not
'''