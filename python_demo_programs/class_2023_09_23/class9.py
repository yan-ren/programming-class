import time

def function1(a=1, b=1):
    if b == 0:
        return

    c = a / b
    d = a + b
    return (a, b, c), d


r1, r2 = function1(b = 5)
print(r1)
print(r2)
# print(function1(1, 2))


# i = 0
# while i < 3:
#     print(i)
#     i += 1 # i = i + 1
#
# print(i)
#
# i = 1
# while i < 100:
#     print(i)
#     i += 2
#
# i = 1
# while i < 100:
#     if i % 2 == 1:
#         print(i)
#     i += 1

i = 10
while i >= 1:
    print(i)
    i -= 1
    time.sleep(1)