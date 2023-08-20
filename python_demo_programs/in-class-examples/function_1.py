def welcome_message():
    print('welcome, are you ready for a question?')


def question(msg):
    welcome_message()
    answer = input(msg)
    print('your answer:' + answer)


def math_calculation(a, b, c):
    d = (a + b) * c
    return d


# call the function
# welcome_message()
# question("what's your name?")
# question("how old are you")
# result = math_calculation(1, 2, 3)
# print(result)

# print(math_calculation(1, 2, 2))
'''
write a function which takes a string as input
then print the number of character in string is even or odd
'''
def check_string_length(s):
    if len(s) % 2 == 0:
        print("even length")
    else:
        print("odd length")

'''
write a function which takes a list of numbers
return the largest value in the list
'''
def largest_value(l):
    max = l[0]
    for num in l:
        if num > max:
            max = num
    return max


print(largest_value([1, 3, 2, 5, 6]))

'''
write a function which takes a list of numbers and return the sum of all numbers
'''
def sum_list(l):
    sum = 0
    for num in l:
        sum = sum + num
    return sum

print(sum_list([1, 2, 3, 4]))

def multiple():
    a = 1
    b = 2
    return a, b

v1, v2 = multiple()
'''
write a function which takes a list of numbers as input
return a new list with only postive numbers

[1, 2, -1, -2]

[1, 2]
'''