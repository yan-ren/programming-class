# n = 0
# s = "kayak"
# palindrome = True
#
# while n < len(s) / 2:
#     if s[n] != s[len(s) - 1 - n]:
#         palindrome = False
#     n += 1
#
# if palindrome:
#     print('palindrome')
# else:
#     print('not palindrome')


def check_panlindrome(input):
    return input[::-1] == input


print(check_panlindrome("kayak"))
print(check_panlindrome("abcd"))