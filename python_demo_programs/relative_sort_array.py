# split the list1 into two parts
def relative_sort_array(list1, list2):
    value_not_in_list2 = []
    common_value = {}
    result = []

    for number in list1:
        if number not in list2:
            value_not_in_list2.append(number)
        else:
            if number in common_value:
                common_value[number] += 1
            else:
                common_value[number] = 1

    for number in list2:
        count = common_value[number]
        while count > 0:
            result.append(number)
            count -= 1

    value_not_in_list2.sort()
    result.extend(value_not_in_list2)
    return result


print(relative_sort_array([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6]))


l1 = [1, 2, 3]
l2 = [1, 2]
l1.extend(l2)
print(l1)