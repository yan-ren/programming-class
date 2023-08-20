# def reverse_string(w):
#     x = w.split(" ")
#     output = ""
#     for i in x:
#         output = output + i[::-1] + " "
#
#     return output
#
#
# print(reverse_string("Let's take LeetCode contest"))

# def reverse_string(string):
#     items = string.split(" ")
#     i = 0
#     while i < len(items):
#         items[i] = items[i][::-1]
#         i += 1
#
#     return ' '.join(items)
#
#
# print(reverse_string("Let's take LeetCode contest"))


def reverse_word(string):
    items = string.split(" ")

    i = 0
    while i < len(items):
        # items[i] = items[i][::-1]
        items[i] = ''.join(reversed(items[i]))
        i += 1

    return ' '.join(items)


print(reverse_word("hello world"))

# s = 'leetcode'
# print(''.join((reversed(s))))
# print(s[0:2])
# print(s[3:6])
# print(s[1:4])
#
# print(s[:2])
# print(s[3:])
#
# print(s[1:5:2])
# print(s[4::-2])
# print(s[::-1])