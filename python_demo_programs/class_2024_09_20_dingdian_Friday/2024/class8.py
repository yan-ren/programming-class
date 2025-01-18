'''
Ask user to enter a number until user enters 'exit'
when user enters 'exit' print the average of all numbers
'''
# sum = 0
# count = 0
#
# while True:
#     user_input = input('Enter a number or type exit to:')
#     if user_input == 'exit':
#         break
#     else:
#         sum += int(user_input)
#         count += 1
#     # print('You entered', user_input)
#
# print(sum / count)

# for i in range(10):
#     print(i)

# s = 'hello'
# for letter in s:
#     print(letter)

# for i in range(1, 11):
#     print(i)
#     i += 1 # wrong, not needed


# i = 0
# while i < 10:
#     print(i)
#     i += 1

# red = int(input())
# green = int(input())
# blue = int(input())
#
# print(red * 3 + green * 4 + blue * 5)

# for i in range(5):
#     if i == 2:
#         continue
#     print(i)

s = 'helloworld'
for letter in s:
    print(letter)

# how to write the same program in while loop
index = 0
while index < len(s):
    print(s[index])
    index += 1

# how to loop through each character in reverse order
index = len(s) - 1
while index >= 0:
    print(s[index])
    index -= 1
    
s_reversed = s[::-1]
for ch in s_reversed:
    print(ch)