# def is_distinct(number):
#     number = str(number)
#     seen = []
#
#     for digit in number:
#         if digit in seen:
#             return False
#         else:
#             seen.append(digit)
#
#     return True
#
# start = int(input())
#
# while not is_distinct(start+1):
#     start += 1
#
# print(start+1)

lines = ['*x*', ' xx', '* *']

size = int(input())
for line in lines:
    new_line = ''
    for ch in line:
        new_line += ch * size

    for i in range(size):
        print(new_line)

