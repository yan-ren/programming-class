# s = "RLRRLLRLRL"
# # list1 = []
# # for char in s:
# #     list1.append(char)
# ans = 0
# count = 0
#
# for i in s:
#     if i == "R":
#         count += 1
#     elif i == "L":
#         count -= 1
#
#     if count == 0:
#         ans += 1
#
# print(ans)


'''
s = 'abcd'
l = ['a', 'b, 'c', 'd']
'''

# s = 'abcd'
# l = list(s)
# print(l)


def balanced_string_split(s):
    balance = 0
    answer = 0
    for i in s:
        if i == "L":
            balance += 1
        else:
            balance -= 1
        if balance == 0:
            answer += 1
    return answer

'''
list comprehension, dictionary comprehension, set comprehension
[expression for loop]
{expression for loop}

'''

'''
exercise1: given a string, create a list using all non-vowel character
s = 'helloworld'
vowel = 'aeiou'
l = ['h', 'l', 'l', 'w', 'r', 'l', 'd']

write above program using list comprehension
'''
s = 'Helloworld'
# l = [ch for ch in s if ch.lower() not in 'aeiou']

'''
[0, 1, 2, 3] -> [1, 3, 5, 7]

[3, 8, 9, 5] -> [True, False, True, False]
'''
l = [3, 8, 9, 5]

[True if n % 3 == 0 else False for n in l]
'''
['apple', 'orange', 'pear'] -> ['A', 'O', 'P']

['apple', 'orange', 'pear'] -> {'apple': 5, 'orange': 6, 'pear': 4}
'''
l = ['apple', 'orange', 'pear']
[w[0].upper() for w in l]
{w:len(w) for w in l}


word="lrlrllrrlr"
l_count=0
r_count=0
res=''
for i in word:
    if i =="l":
        l_count+=1
        res=res+"l"
    if i =="r":
        r_count+=1
        res = res + "r"
    if l_count==r_count:
        print(res)
        res=""



def findNumbers(nums):
    return len([num for num in nums if len(str(num)) % 2 == 0])



n = 10000

def number_of_digits(number):
    digit = 0
    while number > 0:
        number = number // 10
        digit += 1
    return digit

print(number_of_digits(n))

'''
take away:
if question needs to work with integer digit
think about /10 %10
/10 remove the right most digit
%10 get the right most digit
'''