# list = [2, 4, 1, 2, 6]
#
# smallest = list[0]
# second_smallest = list[0]
#
#
# for i in list:
#     if i < smallest:
#         smallest = i
#         second_smallest = smallest
#     elif i < second_smallest:
#         second_smallest = i
#
# print(smallest)
# print(second_smallest)
#
#
# '''
# how to find out the largest and second largest from a list of numbers?
# '''
#
# list = [1, 3, 2, 5, 4]
#
# largest = list[0]
# second_largest = list[0]
#
# for i in list:
#     if i > largest:
#         second_largest = largest
#         largest = i
#     elif i > second_largest:
#         second_largest = i

# list = [1, 3, 2, 5, 4]
# print(list)
# list.sort()
# # list.reverse()
# list[::-1]
# print(list)

def function(number):
    print(number)
    if number == 0:
        return
    else:
        function(number - 1)
        print(number)


function(5)


def countSeniors(details):
    return len([d for d in details if int(d[11:13]) > 60])

'''
data structure:
List, single linked list, double linked list
Hashing
Disjoint set
BST and AVL Tree
Red Back tree(*)

algorithm:
divide and conquer
dynamic programming (memorization)
greedy algorithm

graph algorithm
minimum spanning tree
single source shortest path
bipartite graphs
etc.
'''


def sum(list):
    result = 0
    for i in list:
        result += i

    return result


sum([1])
sum([1, 20, 100])

'''
O(N), N is the size of input, when N increase, the runtime increase linearly
'''

def sum(matrix):
    result = 0
    for row in matrix:
        for col in row:

            result += col

    return result

'''
O(N^2), N is the size of input, when N increase, the runtime increase quadratically

The run time of an algorithm is stated as a function relating the input length the the time complexity
The algorithm complexity can be three parts: best case, average case, worst case

Big 0 notation can be expressed the upper bound of the run time
'''
def is_even(number):
    return number % 2 == 0

'''
O(1) constant run time
'''

'''
compare following two program
assume a problem can be solved by following two solution
'''
'''
O(N+N) ~ O(N)
'''
def solution1(n):
    for i in n:
        pass

    for i in n:
        pass

'''
O(N*N)
'''
def solution2(n):
    for i in n:
        for j in n:
            pass


'''
O(10N) ~ O(N)
'''
def solution3(n):
    for i in n:
        for j in range(10):
            pass



