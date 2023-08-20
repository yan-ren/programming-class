'''
Given a string s, find the first non-repeating character in it and return its index

example:
s = "leetcode"
return 0



s = "aabccd"
return 2

s = "aeac"

return 1
'''

def first_unique_char(s):
    dict = {}
    for ch in s:
        if ch in dict:
            dict[ch] += 1
        else:
            dict[ch] = 1
    '''
    {'a': 2, 'b': 1}
    '''
    i = 0
    while i < len(s):
        if dict[s[i]] == 1:
            return i
        i += 1

'''
a: string
n: length of string
'''
def unique(a, n):
    for i in range(n):
        j = i
        while j < n:
            if i != j and a[i] == a[j]:
                break
            else:
                j += 1

        if j == n:
            return i

'''
recursion definition: a function calls itself, then we call this function recursive function
two 

base case:
recursive case:

'''
def print_str(str):
    print_str(str)


# print_str("hello")

'''
input: abc

reverse(abc) = reverse(bc) + 'a'
reverse(bc) = reverse(c) + 'b'
reverse(c) -> base case

return: cba
'''
# def reverse_str(str):
#     if len(str) == 1:
#         return str
#     else:
#         return reverse_str(str[1:]) + str[0]


word="hehalpeloo"
dict={}
count=0
first=''
for i in word:
    if i not in dict:
        dict[i]=1
    else:
        dict[i]+=1

for i,j in dict.items():
    if j==1:
        first=i

for i in word:
    if first==i:
        print(count)
    count+=1

'''
Fibonacci Number
1, 1, 2, 3, 5, ....
'''
# return nth fibonacci number
'''
fib(n) = fib(n-1) + fib(n-2)
fib(n-1) = fib(n-2) + fib(n-3)
fib(n-2) = fib(n-3) + fib(n-4)
...
fib(2) = 1
fib(1) = 1

'''
# def fib(n):

'''
factorial n!
5! = 5*4*3*2*1

'''