input = [10, 3, 9, 8, 9, 9]

a_score = input[0] * 3 + input[1] * 2 + input[2]
b_score = input[3] * 3 + input[4] * 2 + input[5]

if a_score > b_score:
    print("A")
elif b_score > a_score:
    print("B")
else:
    print("T")