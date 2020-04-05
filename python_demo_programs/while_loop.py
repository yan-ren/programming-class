# import time
# # module
# n = int(input('enter a number:'))
#
# while n > 0:
#     print(n)
#     time.sleep(1)
#     n -= 1
n = 2
while n < 100:
    print(n)
    n += 2

# method 2
n = 1
while n < 100:
    if n % 2 == 0:
        print(n)
    n += 1