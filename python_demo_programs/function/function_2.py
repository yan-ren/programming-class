# parameter = variable inside the bracket
# argument
# input
# def welcome_msg(name):
#     print('hello, ' + name)
#     print('welcome to the programming class')
#
#
# def welcome_msg_1(name, classname):
#     print('hello, ' + name)
#     print('welcome to the ' + classname)
#
#
# welcome_msg_1("gary", "programming class")
# welcome_msg_1("gary", "math class")

# write a function finds the largest value among three values
def find_largest(a, b, c):
    if a > b and a > c:
        print(a)
    elif b > a and b > c:
        print(b)
    else:
        print(c)


find_largest(1, 2, 3)
find_largest(10, 9, 7)

# write a function gives the sum of all elements in a list
def sum_list(a):
    sum = 0
    for i in a:
        sum += i
    print(sum)

sum_list([1, 2, 3, 4])
sum_list([10, 20, 30, 40])
