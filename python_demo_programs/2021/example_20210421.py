'''
write a python function that takes a string and returns a dictionary
the dictionary key is the each character in the string, the value is the frequency of the character

s = "abbc"
d = {"a": 1, "b": 2, "c": 1}

s = "hello"
d = {"h": 1, "e": 1, "l": 2, "o": 1}
'''


def foo():
    # for the same variable in a function, it has to be on the same scope all the time
    print(s) # local s
    s = "Me too." # python analysis the complete program find out you define a local s here
    print(s) # local s


s = "I hate spam."
foo()
print(s)

