test_group = int(input())
test_inputs = []

# collect input for all test group
for _ in range(test_group):
    cars = []
    num_cars = int(input())
    for _ in range(num_cars):
        cars.append(int(input()))
    test_inputs.append(cars)

for mountain_top in test_inputs:
    branch = []
    expected_car = 1

    while True:
        if mountain_top:
            if mountain_top[len(mountain_top)-1] == expected_car:
                mountain_top.pop()
                expected_car += 1
            elif branch and branch[len(branch)-1] == expected_car:
                branch.pop()
                expected_car += 1
            else:
                branch.append(mountain_top.pop())
        elif branch:
            if branch[len(branch)-1] == expected_car:
                branch.pop()
                expected_car += 1
            else:
                print('N')
                break
        else:
            print('Y')
            break

