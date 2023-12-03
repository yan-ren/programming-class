import time

i = 0
while i < 10:
    print(i)
    i = i + 1

# print all odd numbers under 100
# option 1
# i = 1
# while i < 100:
#     print(i)
#     i += 2

# option 2
# i = 0
# while i < 100:
#     if i % 2 == 1:
#         print(i)
#     i += 1

# write a countdown program, meaning ask user for a number then count down from that number to zero
number = int(input("Enter for countdown:"))
while number > 0:
    print(number)
    number -= 1
    time.sleep(1)

# exercise: print all numbers under 100 that is multiple of 5
number = 0
while number < 100:
    if number % 5 == 0:
        print(number)
    number += 1

