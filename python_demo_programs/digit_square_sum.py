def happy_number():
    input_n = list(input())
    sum_of_inputs = 0
    for i in input_n:
        sum_of_inputs += int(i)**2

    return sum_of_inputs

print(happy_number())
