
# # dictionary pairs have int key, string value
# sample = {0: "Yan", 1: "Gary", 2: "Gilbert", 3: "Hangbing", 4: "Justin", 5: "Nick", 6: "Yijun Zhu"}
# print(sample[5])
# # add a new key-value pair
# sample[7] = "new student"
# print(sample[7])
#
# sample[7] = "new teacher"
# print(sample[7])
#
# sample2 = {"key": "value"}
# sample3 = {1: "one", 2: 2}
#
# # about the key, python defines only immutable item can be the key
# # for example, list is mutable, so you cannot have list as dictionary key
# sample4 = {(1, 2): 1}
# sample5 = {1: [1, 2, 2]}

# practice, create a dictionary using loop, who has the content {0 : 1, 1 : 2, 2 : 3, ... 9: 10}
# sample6 = {}
# for i in range(9):
#     sample6[i] = i + 1
#
# print(sample6)

# sample = {1:100, 2:200}
# print(sample[1])
# print(sample.get(1))
#
# # print(sample[0])
# print(sample.get(100, "value not exists"))
# # del sample[1]
# v = sample.pop(1)
# print(v)
# print(sample)

# homework: create a dictionary using loop,
# where the sum of each key and value equals to 10
# example:
# d = {0: 10, 1:9, 2: 8, 3: 7, 4: 6, 5:5, 6:4, 7:3, 8:2, 9:1, 10:0}

d = {"one": 1, "two": 2, "three": 3}
l = list(d.keys())
print(type(l))
print(l)