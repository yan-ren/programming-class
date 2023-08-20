def convert_input(list1, list2):
    dic = {}
    for i in list1:
        if i not in list2:
            dic[i] = -1
        else:
            dic[i] = list1.index(i)

    for j in list2:
        if j in dic:
            for key, value in dic.items():
                if j == key:
                    dic[key] = value + list2.index(j)
                    break

        else:
            dic[j] = -1

    dic1 = {}
    for keys, values in dic.items():
        if values >= 0:
            dic1[keys] = values

    return dic1


def find_output(list1, list2):
    output = []
    source = convert_input(list1, list2)
    minimum = len(list1) + len(list2)
    for value in source.values():
        if value < minimum:
            minimum = value

    for key, value in source.items():
        if value == minimum:
            output.append(key)

    for i in output:
        print(i)