import math

# lab8
# m = float(input('Enter the box mass'))
# mu = float(input('Enter the coefficient of friction'))
#
# g = 9.8
# T = 30
#
# angle = 0
# a_largest = 0
# best_angle = 0
# while angle < 90:
#     theta = math.radians(angle)
#     a = (T * math.cos(theta) - mu * (m * g - T * math.sin(theta)) ) / m
#     if a > a_largest:
#         a_largest = a
#         best_angle = angle
#     angle += 0.1
#
# if a_largest > 0:
#     print('The max acceleration is', round(a_largest, 2), 'm/s at', round(best_angle, 2), 'degrees')
# else:
#     print('The box will not move')

numbers = [4, 2, 5, 3, 1]
num_largest = numbers[0]
num_second_largest = numbers[0]

for number in numbers:
    if number > num_largest:
        num_second_largest = num_largest
        num_largest = number
    elif number > num_second_largest:
        num_second_largest = number

print(num_largest)
print(num_second_largest)