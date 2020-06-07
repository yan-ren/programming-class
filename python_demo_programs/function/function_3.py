def pulse(a, b):
    c = a + b
    print('hello')
    return c


# three things to consider when writing functions
# function name
# input? one, two, or more
# return?

# write a function that reverse a string
def reverse_str(string):
    return string[::-1]


print(reverse_str("hello"))

# write a function that finds the largest value in a list
def find_max(res):
    # check empty
    if len(res) == 0:
        return 0

    max = res[0]
    for i in res:
        if i > max:
            max = i
    return max

print("happy monther's day")
