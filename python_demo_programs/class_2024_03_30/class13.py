# x = 6
# y = x / (x - 6)
# print(y)

# def foo():
#     x = "hello"
#     return x
#
#
# x = foo()
# print(x)

# def my_divide(a, b):
#     if b == 0:
#         raise TypeError
#
#     return a / b
#
#
# try:
#     my_divide(2, 1)
# except TypeError:
#     print('There is an exception')
#
# print('done')

# while True:
#     try:
#         x = int(input('Give a number:'))
#         break
#     except ValueError:
#         print('Try again')


'''
Problem Statement
You need to write a function that safely retrieves a value from a dictionary given a key. 
The function should handle cases where the key is not found using try and except blocks.

Instructions
Write a function called safe_dict_lookup that takes two arguments: dictionary (a dictionary) and key (the key to look up).
Use a try block to attempt to retrieve the value associated with the key from the dictionary.
If a KeyError occurs (i.e., the key is not found), catch the exception and return the string "Key not found".
If the key is found, return the value.
'''
def safe_dictionary_look(dic, key):
    if key not in dic:
        raise KeyError

    return dic[key]

def safe_dic_lookup(dic, key):
    try:
        return dic[key]
    except KeyError:
        return 'Key not found'

# print(safe_dic_lookup({'a': 1}, 'b'))


def safe_list_access(lst, index):
    try:
        return lst[index]
    except IndexError:
        return 'index out of range'


def divide_number(a, b):
    try:
        result = a / b
        return result
    # except ZeroDivisionError:
    #     return 'cannot divide by zero'
    # except TypeError:
    #     return 'a or b cannot be divided'
    except Exception as error:
        return error

print(divide_number(1, 0))