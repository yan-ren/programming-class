# name = 'Tom'
# age = 20
#
# print('My name is ' + name + ' I am ' + str(age) + ' years old')
# print(f'My name is {name}')
#
# a = 2
# b = 4
# print(f'a * b = {a * b}')
#
# data = [
#     ['Alice', 30, 'New York'],
#     ['Bob', 25, 'Los Angeles'],
#     ['Charlie', 35, 'Chicago']
# ]
# #|------------|--------|----------------|
# sep = f'|{'-'*12}|{'-'*8}|{'-'*16}|'
#
# print(sep)
# print(f"|{"Name":<12}|{"Age":<8}|{"City":<16}|")
# print(sep)
#
# for name, age, city in data:
#     print(f"|{name:<12}|{age:<8}|{city:<16}|")
# print(sep)
#
# x = 1.2345
# print(f'{x:10.2f}')
#
# d = {
#     'Alice': 2,
#     'Bob': 4
# }
#
# for key, value in d.items():
#     print(key, value)

import matplotlib.pyplot as plt

fruits = ['Apples', 'Bananas', 'Cherries', 'Dates']
sales = [45, 652, 28, 51]

plt.bar(fruits, sales)
plt.title('fruit sales')
plt.ylabel('Units sold')
plt.show()

languages = {'Python': 85, 'Java': 70, 'C++': 55, 'JavaScript': 90}

plt.barh(list(languages.keys()), list(languages.values()),
         color=['b', 'r', 'g', 'orange'])
plt.title("Language Popularity Score")
plt.show()

sizes = [40, 25, 20, 15]
labels = ['Rent', 'Food', 'Transport', 'Savings']

plt.pie(sizes, labels=labels, labeldistance=1.3)
plt.title("Monthly Budget")
plt.show()

n = 15
x = [0] * n
y = [0] * n
z = [0] * n

for i in range(n):
    x[i] = i
    y[i] = i * 2
    z[i] = i ** 1.5

plt.plot(x, y, 'b--s')   # blue, dashed, square markers
plt.plot(x, z, 'r:.')    # red, dotted, point markers
plt.legend(['Linear', 'Power 1.5'])
plt.xlabel("x")
plt.ylabel("y")
plt.show()


hours_studied = [1, 2, 3, 4, 5, 6, 7, 8]
grades = [52, 58, 65, 70, 73, 82, 88, 91]

plt.scatter(hours_studied, grades)
plt.xlabel("Hours Studied")
plt.ylabel("Exam Grade (%)")
plt.title("Study Time vs. Grade")
plt.show()

# subplots
x = list(range(1, 11))
squares = [v ** 2 for v in x]
cubes = [v ** 3 for v in x]

plt.subplot(1, 2, 1)
plt.plot(x, squares, 'g-o', markerfacecolor='none')
plt.title('squares')

plt.subplot(1, 2, 2)
plt.plot(x, cubes, 'r--^')
plt.title('Cubes')

plt.tight_layout()
plt.show()