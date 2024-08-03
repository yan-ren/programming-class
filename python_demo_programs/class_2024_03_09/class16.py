# A_FREE = 100
# A_DAYTIME = 15
# A_EVENING = 20
# A_WEEKEND = 25
#
# B_FREE = 200
# B_DAYTIME = 20
# B_EVENING = 25
# B_WEEKEND = 30
#
# C_FREE = 250
# C_DAYTIME = 30
# C_EVENING = 35
# C_WEEKEND = 40
#
# daytime = int(input('Number of daytime minutes?'))
# evening = int(input('Number of evening minutes?'))
# weekend = int(input('Number of weekend minutes?'))
#
# plan_a = (daytime - A_FREE) * A_DAYTIME + evening * A_EVENING + weekend * A_WEEKEND
# plan_b = (daytime - B_FREE) * B_DAYTIME + evening * B_EVENING + weekend * B_WEEKEND
# plan_c = (daytime - C_FREE) * C_DAYTIME + evening * C_EVENING + weekend * C_WEEKEND
#
# print('Plan A costs', plan_a)
# print('Plan B costs', plan_b)
# print('Plan C costs', plan_c)
#
# if plan_a < plan_b and plan_a < plan_c:
#     print('choose Plan A')
# elif plan_b < plan_a and plan_b < plan_c:
#     print('choose Plan B')
# else:
#     print('choose Plan C')


'''
Write a function that takes a list of numbers as input, 
return how many even number in the list
 %
'''

# def find_even(numbers):
#     count = 0
#     for num in numbers:
#         if num % 2 == 0:
#             count += 1
#     return count

'''
Exercise: write a function that takes two numbers lists as inputs, 
compare which list's total sum is bigger
'''
def sum(list):
    res = 0
    for value in list:
        res += value

    return res

def compare_list_sum(list1, list2):
    if sum(list1) > sum(list2):
        return list1
    else:
        return list2


