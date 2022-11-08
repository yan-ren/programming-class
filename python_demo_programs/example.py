# numbers = [2, 3, 4, 1, 6]
# numbers.sort()

# # decendent
# numbers.sort(reverse=True)

# #
# numbers.sort()
# numbers.reverse()


# words = ["abc", "five", "earth", "a"]
# words.sort()
# print(words)

# words.sort(key=len)
# print(words)

numbers = [(2, 2), (3, 4), (4, 1), (1, 3)]

def first_value(e):
    return e[0]

numbers.sort(key=first_value)
print(numbers)

# sort list of tuples basing on the sum of tuples, each tuple contains two value
numbers = [(1, 2), (2, 3), (3, 4)]
# def sum_of(e):
#     return(sum(e))

# numbers.sort(key=sum)
# print(numbers)

# employees = [
#     {'Name': 'Alan Turing', 'age': 25, 'salary': 10000},
#     {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000},
#     {'Name': 'John Hopkins', 'age': 18, 'salary': 1000},
#     {'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000},
# ]

# # sort list of dictionary base on age
# def get_age(e):
#     return e['age']

# employees.sort(key=get_age)
# print(employees)

# print(1, 2, sep="@")

# list = [10, 20, 30, 40]
# a, *b = list
# a, *b, c = list
# print(a, b, c)

# for i in range(5):
#     print(i)
#     if i == 2:
#         break
# else:
#     print('finish')

# a = {1:11, 2:22, 3:33, 4:33}
# b = {j:i for i, j in a.items()}

# print(b)

a = [1, 2, 3]
# this function creates a copy of a and assign to b
# so a and b points to different list object
b = a.copy()