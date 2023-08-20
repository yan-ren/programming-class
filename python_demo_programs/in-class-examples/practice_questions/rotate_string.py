def shift(string):
    if len(string) == 0:
        return string
    else:
        return string[1:] + string[0]


# print(shift("abcde"))

def rotate_string(s, goal):
    for i in s:
        if s == goal:
            return True
        s = shift(s)

    return False

# example1
print(rotate_string("abcde", "cdeab"))

# example2
print(rotate_string("abcde", "abced"))
