# # mutable
# l = [1, 2, 30, 40]
# l.append(50)
# print(l)
#
# # immutable
# t = (1, 2, 30, 40)
# for number in t:
#     print(number)
#
# dic = {}
# dic['two'] = 2
# print(dic)


# def calculation(a, b):
#     return a+b, a*b
#
#
# num1, num2 = calculation(1, 2)
# print(num1, num2)
#
# t = 1, 2
# print(type(t))

a = 1
b = 2

a, b = b, a
print(a)
print(b)

'''
Find most frequent letter in string
Given a string s, return the most frequent letter in s

'''
def frequent_letter(s):
    frequency = {}

    # iterate each char in string
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    print(frequency)

    # find the char with the highest frequency
    most_frequent = None
    max_count = 0

    for char, count in frequency.items():
        if count > max_count:
            most_frequent = char
            max_count = count

    return most_frequent


print(frequent_letter('aababc'))

'''
Merge two dictionaries
Write a function that merges two dictionaries. If a key is present in both dictionaries, sum the value

e.g.
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}

dict3 = {'a': 1, 'b': 5, 'c': 7, 'd': 5}
'''
def merge_dictionaries(d1, d2):
    new_dic = {}
    for key, value in d1.items():
        new_dic[key] = value

    for key, value in d2.items():
        if key in new_dic:
            new_dic[key] += value
        else:
            new_dic[key] = value

    return new_dic


dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}

print(merge_dictionaries(dict1, dict2))
