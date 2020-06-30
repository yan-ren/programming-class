# greeting = 'hello world'
# s = greeting.replace('llo', 'y')
# print(s)
# print(greeting)

# practice: given a string s, replace all number 1 with letter a
# s = '11234abcde'
# # 'aa234abcde'
# s = s.replace('1', 'a')
# print(s)
#
# s = 'hello hello hello'
# print(s.find('lo'))

# problem: write a python function to get a string made of the first 2 and the last 2 chars from a given string
# given string: 'helloworld'
# result string: 'held'
# if your string is less than 4 chars, e.g. 'abc', return an empty string ''

def make_string(string):
    if len(string) < 4:
        return ''
    else:
        return string[:2] + string[len(string)-2:]

print(make_string('helloworld'))

# problem: write a python function to get a string from a give string where all occurrence of its first char have ben changed to '$'
# except for the first char
# given string: 'restart'
# easier version: '$esta$t'
# complete version: 'resta$t'
# given string: 'kayak'
# result: '$aya$'