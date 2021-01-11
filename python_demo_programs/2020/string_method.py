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
        return string[0] + string[1] + string[len(string) - 2] + string[len(string) - 1]

# def make_string(string):
#     if len(string) < 4:
#         return ''
#     else:
#         return string[:2] + string[len(string)-2:]
#
# print(make_string('helloworld'))

# problem: write a python function to get a string from a give string where all occurrence of its first char have ben changed to '$'
# except for the first char
# given string: 'restart'
# easier version: '$esta$t'
# complete version: 'resta$t'
# given string: 'kayak'
# result: '$aya$'

# def replace_dollar(string):
#     return string.replace("r", "$")
#
#
#
# print(replace_dollar("restart"))
#
# s = "   abcd   "
# # remove the leading/tailing space and 'a'
# print(s.strip('a '))
#
# print(s)


# date = '2020-02-20'
# date = date.split('-')
# print(date)
# if date[0] == '2020':
#     print('date is in current year')

# l = ['a', 'b', 'c']
# print(''.join(l))

string = '2020-02-14'
print(string.split('-'))

# write a function takes two string in date format, e.g '2020-02-02' compare which year is earlier
# '2020-02-01' '1992-02-01'
def compare_date(date1, date2):
    date1 = date1.split('-')
    date2 = date2.split('-')

    if date1[0] < date2[0]:
        print('date1 is earlier')
    else:
        print('date2 is earlier')

# write a function takes an integer list, remove all the even number and return as a string
def process_list(list):
    for i in list:
        if int(i) % 2 == 0:
            list.remove(i)
    return ''.join(list)

print(process_list(['1', '2', '3', '4']))
# homework reading: slides 1.1 page 139-151
# question: write a function takes a mixed list with numbers and string, remove all the numbers from the list
# example input: [1, 2, 'a', 'b']
# output: ['a', 'b']

# a is an integer type and a is an instance of integer
a = 1
b = 'abc'
print(isinstance(a, int))
print(isinstance(b, int))

def filter(list):
    res = []
    for i in list:
        if not isinstance(i, int):
            res.append(i)

    return res
