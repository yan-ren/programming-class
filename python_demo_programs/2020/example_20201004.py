# what is a function/method
# group some code together for re-use

# write a function that counts how many of letter "a" in string
def count(input):
    counter = 0
    for i in input:
        if i == "a":
            counter += 1

    return counter


print(count("ababa"))
print(count("abcdefa"))

# write a function that takes two variables, two strings,
# check if first string contains second string
# abc, ab -> True
# abc, ad -> False
# q: how to check if one string contains another'
def isContained(first, second):
    return second in first


# list = []
# print(list)
# list.append(1)
# print(list)
# print(list[0])
# del list[0]
# print(list)

# write a function that returns the largest value in the list
# [2, 3, 4, 5] -> 5
def max(list):
    max = list[0]
    for i in list:
        if i > max:
            max = i

    return max

# write a function that takes a list as input,
# return how many string in list has letter "a"
# ['abc', 'xyz', 'aba', '1221'] -> 2
# count function return 0 -> no letter "a" in string
def a_in_list(list):
    counter = 0
    for s in list:
        if count(s) > 0:
            counter += 1
    return counter

# Write a Python function to multiplies all the items in a list.
# [1, 2, 3, 4] -> 24
def multiplies(list):
    result = 1
    for i in list:
        result = result * i

    return result

# Write a Python function to sums all the items in a list.
# [1, 2, 3, 4] -> 100
def sums(list):
    result = 0
    for i in list:
        result += i
    return result

# Write a function returns the second largest
list = [10, 20, 30, 40]
del list[0]
list.remove(40)
# step: find the largest, remove, find largest again
def second_largest(list):
    largest = max(list)
    list.remove(largest)
    largest = max(list)
    return largest

# write a function returns the sum of all even indexed value
# [10, 20, 30, 40, 50, 60]
# 10, 30, 50 have even index, return 90
def even_sum(list):
    index = 0
    sum = 0
    while index < len(list):
        if index % 2 == 0:
           sum += list[index]
        index += 1

    return sum

def even_sum2(list):
    index = 0
    sum = 0
    for i in list:
        if index % 2 == 0:
           sum += i
        index += 1

    return sum