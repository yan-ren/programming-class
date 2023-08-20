'''
Average calculator, e.g. user keeps entering numbers until enter a finish word, such as “end”. 
Calculate the average basing on all user inputs
'''
# finish = False
# sum = 0
# count = 0

# # not False -> True
# # not True -> False
# while not finish:
#     value = input("enter a number or enter 'end' to finish the program: ")
#     # value -> string
#     if value == 'end':
#         finish = True
#     else:
#         # int(), convert string to number
#         sum += int(value)
#         count += 1

# # calculate the average using sum and count
# print(sum / count)


# string indexing
# each character in string has a number associated with it
s = "abcde"
# print(s[0])

# how to using while loop, to access(print) each character in string
# print(len(s))
# largest index = len(s) - 1
# index = 0

# while index < len(s):
#     print(s[index])
#     index += 1

# # how to print each character in string in reverse order
# index = len(s) - 1

# while index >= 0:
#     print(s[index])
#     index -= 1

# nested while loop: while loop inside while loop
# i = 0
# while i < 5:
#     j = 0
#     while j < 3:
#         print(j)
#         j += 1
#     i += 1

# break, continue

# break: finish the loop
# i = 0
# while i < 10:
#     if i == 5:
#         break
#     print(i)
#     i += 1

# coutinue: finish the current iteration
# i = 0
# while i < 10:
#     i += 1
#     if i == 5:
#         continue
#     print(i)

# practice: print all odd number under 10 using continue and while loop
# i = 0
# while i < 10:
#     i += 1
#     # when i is even, skip the current loop using continue
#     if i % 2 == 0:
#         continue
#     print(i)

arr = [0, 2, 3, 4, 5, 2, 1, 0]
left_index = 0

while left_index < len(arr) - 2 and arr[left_index] < arr[left_index + 1]:
    left_index += 1

right_index = len(s) - 1
while right_index > 0 and arr[right] < arr[right_index - 1]:
    right_index -= 1

if left_index == right_index:
    print(True)
    
print(False)