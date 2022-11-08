'''
scope: visibility of a variable
'''
# x = 2 # global scope
# def test():
#     x = 3
#     # local scope of function test
#     print(x)
#     y = 2
#     print(globals()['x'])
#     return y
#
#
# t = test()
# print(x)
# print(t)
# def a():
#     print("a")
#     a()
import sys

'''
recursion: a function calls itself 
'''


# def b():
#     print("b")
#
#
# a()
'''
Write a Python function to reverse a string.
Sample String : "1234abcd"
Expected Output : "dcba4321"
'''


'''
delimiter
'this is a string'

split
 
['this', 'is', 'a', 'string']
'''
# def reorganize_sentence(string):
#     # "is2 sentence4 This1 a3"
#     dic = {}
#     l = string.split()
#     # ['is2', 'sentence4', 'This1', 'a3']
#     for i in l:
#         dic[int(i[len(i)-1])] = i[:len(i)-1]
#
#     # {2: 'is', 4: 'sentence', 1: 'This', 3: 'a'}
#     # range(1, 5)
#     # for j in range(1, len(l)+1):
#     #     l[j-1] = dic.get(j)
#
#     # sort the key and use the sorted key
#     for key in sorted(dic.keys()):
#         l[key-1] = dic[key]
#     return " ".join(l)
#
#
# print(reorganize_sentence("is2 sentence4 This1 a3"))
#
# def reorganize_sentence_1(s):
#     l = s.split()
#     new_l = [''] * len(l)
#
#     for i in l:
#         new_l[int(i[len(i) - 1])-1] = i[:len(i) - 1]
#
#     return ' '.join(new_l)
#
# print(reorganize_sentence_1('is2 sentence4 This1 a3'))

'''
if a language supports first-class functions
- functions can be passed as arguments to other functions
- functions can be returned as the values from other functions
- functions can be assigned to variables

objects can do above things

in python functions are objects
'''
# def shout(text):
#     return text.upper()
#
#
# def whisper(text):
#     return text.lower()
#
#
# def greet(f):
#     print(f('hello'))
#
#
# greet(shout)
# greet(whisper)
#
#
# def create_adder(x):
#     def adder(y):
#         return x+y
#
#     return adder
#
#
# add_15 = create_adder(15)
# add_20 = create_adder(20)
# print(add_15(10))
#
# g = greet


'''
Exception handling

syntax error
logical error: errors that happen at runtime, are called exceptions
built-in exception

'''
# l = [1, 2, 3]
# print(l[4])
# print(1/0)
# print(dir(locals()['__builtins__']))
# l = ['a', 0, 2]
#
# for value in l:
#     try:
#         result = 1 / int(value)
#         print(result)
#     except Exception as e:
#         print(e)
#         print("have some error")
#     finally:
#         print("in finally")

'''
s = "is2 sentence4 This1 a3"

['is2', 'sentences4', 'This1', 'a3']
'''
def reorganize_sentence(sentence):
    words = sentence.split(" ")
    result = [''] * len(words)

    for word in words:
        num = word[len(word)-1:]
        letter = word[:len(word)-1]
        result[int(num)-1] = letter

    print(result)
    " ".join(result)

reorganize_sentence("is2 sentence4 This1 a3")
