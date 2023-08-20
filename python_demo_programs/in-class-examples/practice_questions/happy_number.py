# def happy_number(input_n):
#     input_n = list(str(input_n))
#     sum_of_inputs = 0
#     for i in input_n:
#         sum_of_inputs += int(i)**2
#     return sum_of_inputs
#
#
# def identify():
#     input_number = int(input())
#     source = []
#
#     while happy_number(input_number) != 1:
#         if happy_number(input_number) not in source:
#             source.append(input_number)
#             input_number = happy_number(input_number)
#         else:
#             return 'not happy number'
#
#     return 'happy number'
#
#
# print(identify())

def digit_square_sum(input_n):
    input_n = list(str(input_n))
    sum_of_inputs = 0
    for i in input_n:
        sum_of_inputs += int(i)**2
    return sum_of_inputs


seen = []
num = int(input())
while True:
    num = digit_square_sum(num)
    if num in seen and num != 1:
        print("not happy number")
        break
    elif num == 1:
        print("happy number")
        break
    else:
        seen.append(num)

