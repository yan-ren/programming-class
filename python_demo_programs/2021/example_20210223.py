# x = 47320
# y = "hello"
#
# print(x)
# print(1 is 1.0)

m = [1, 2, 3]
n = [1, 2, 3]
m[0] = 100
# because n and m points to the same object
# the change through m is also visible to n
print(n)

'''
Write a Python script to concatenate following dictionaries to create a new one.

Sample Dictionary:
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50, 6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
'''
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

merged_dic = {}

for dic in [dic1, dic2, dic3]:
    for k, v in dic.items():
        merged_dic.update({k: v})

# Test 1
print(merged_dic)