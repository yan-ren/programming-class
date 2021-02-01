# old = [2, 4, 6, 8, 9]
# # create a new list with each element from the old subtracted by one
# # new = [1, 3, 5, 7, 8]
# # 1. create new list
# # 2. loop through the old list
# # 3. add each value to new list by subtracted one
# def minus(x):
#     return x -1
#
#
# new = []
# for i in old:
#     new.append(minus(i))
#
# new = [minus(i) for i in old]
# print(new)
#
# # create a new list with element bigger than 3 from the old list and subtracted by one
# # new = [3, 5, 7, 8]
# new = []
# for i in old:
#     if i > 3:
#         new.append(minus(i))
#
# new = [minus(i) for i in old if i > 3]

# numbers = [1, 2, 3, 4, 5, 6, 7]
# create a new list with numbers between 3 to 5 (included)
# new = [3, 4, 5]
# new = []
# for i in numbers:
#     if 3 <= i <= 5:
#         new.append(i)
#
# new = [i for i in numbers if 3 <= i <= 5]

# new = ['even' if i%2==0 else 'odd' for i in numbers]
# print(new)

# sentence = ['abc', 'ABC']
# a = [word.lower() for word in sentence]

word = 'hello'
a = [ch for ch in word.lower() if ch not in 'aeiou']
print(a)
