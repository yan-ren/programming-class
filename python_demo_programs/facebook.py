import math

def build_dic(string):
    dic = {}
    for s in string:
        if s in dic:
            dic[s] += 1
        else:
            dic[s] = 1

    return dic


facebook = "facebook"
target = "cakebook"

facebook = build_dic(facebook)
target = build_dic(target)

max = 0
for key, value in target.items():
    value_in_fb = facebook[key]
    if math.ceil(value / value_in_fb) > max:
        max = math.ceil(value/value_in_fb)

print(max)
