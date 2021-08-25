'''
given a list of string in email format
['yan@gmailcom', 'yan@hotmail.com', 'yan@live.com', 'tom@gmail.com']

create a dictionary where the key the is user name, value is the list of emails for the user
{'yan':['yan@gmail.com', 'yan@hotmail.com',
    'yan@live.com'], 'tom': ['tom@gmail.com']}

hint:
string.split
'''
# text = "welcome to the jungle"
# x = text.split('to')
# print(x)
# input = ['yan@gmail.com', 'yan@hotmail.com', 'yan@live.com', 'tom@gmail.com']
# result = {}
# for email in input:
#     element = email.split('@')
#     if element[0] not in result:
#         result[element[0]] = [email]
#     else:
#         result[element[0]].append(email)

# given a string e.g. "hello", generate a dictionary where the key is the character, value is the frequency of character
# {'h':1, 'e':1, 'l':2, 'o':1}


class Dog:
    def __init__(self, name):
        self.name = name
        self.tricks = []

    def teach_trick(self, trick):
        self.tricks.append(trick)

    def _internal_method(self):
        pass

    def __str__(self):
        return self.name

    def __eq__(self, another_dog):
        return self.name == another_dog.name


dog1 = Dog("bob")
dog1.teach_trick("bark")
print(dog1)

dog2 = Dog("bob")

print(dog1 == dog2)

# don't want
# dog._internal_method()
# dog._name

# magic method in python are the special methods that start and end with double underscores

'''
given two sorted list, merge them into a single sorted list (don't use sort method)
num1 = [1, 2, 3]
num2 = [2, 5, 6]

num3 = [1, 2, 2, 3, 5, 6]
'''
num1 = [1, 2, 3]
num2 = [2, 5, 6]
result = []
index1 = 0
index2 = 0

while index1 < len(num1) and index2 < len(num2):
    if num1[index1] < num2[index2]:
        result.append(num1[index1])
        index1 += 1
    else:
        result.append(num2[index2])
        index2 += 1

while index1 < len(num1):
    result.append(num1[index1])
    index1 += 1

while index2 < len(num2):
    result.append(num2[index2])
    index2 += 1
