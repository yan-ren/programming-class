
def count_prefixes(words, s):
    # count = 0
    # for word in words:
    #     if s.startswith(word):
    #         count += 1
    #
    # return count
    return [s.startswith(word) for word in words].count(True)


print(count_prefixes(['a', 'b', 'c', 'ab', 'bc', 'abc'], 'abc'))
'''
startswith -> boolean
comprehension -> list

-> list of boolean -> list.count()
'''


'''
if s1 starts with s2, then return true
otherwise return false

e.g.
s1="abc"
s2="ab"
return True

s1="abc"
s2="abcde"
return False
'''
# def startswith(s1, s2):
#     index = 0
#     for char in s1:
#         if char != s2[index]:
#             return False
#         index += 1
#
#         if index > len(s2):
#             return True
#
#     return True


def startswith(s1, s2):
    if len(s1) < len(s2):
        return False

    if s1[:len(s2)] == s2:
        return True
    return False


# print(startswith('abc', 'ab'))
# words = ["a","b","c","ab","bc","abc"]
# s = "abc"
# print(count_prefixes(words, s))

# f = open('text.txt')
# for line in f:
#     print(line)
# f.close()

with open('text.txt', 'w') as f:
    f.write('this is the line we are writing to')
