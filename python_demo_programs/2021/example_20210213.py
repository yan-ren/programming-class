# x = 47320 # number 47320 is an integer object with value 47320
# print(id(x))
# print(x)
# y = "Hello"
# print(id(y))
# print(locals())

# x = 1
# y = 1.0
# print(id(x))
# print(id(y))
# print(x is y)
# print(x == y)

# x = "hello world"
# y = "hello "
# print(id(x))
# print(id(y))
# y += "world"
# print(id(x))
# print(id(y))

# x = 1000
# y = x
# x = 100
# # x points to a new object,
# # why old object x cannot change value from 1000 to 100?
# # because 1000 is an integer object, immutable
# print(x)
# print(y)
#
# x = [1]
# y = x
# x.append(2)
# print(x)
# print(y)

def ref_demo(x):
    print("x=", x, "id=", id(x))
    x = 42
    print("x=", x, "id=", id(x))
    return x

x = 9
print(id(x))
y = ref_demo(x) # pass x's copy into method
print(id(x))
print(id(y))

'''
Given an list of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Input: nums = [3,2,4], target = 6
return [1, 2]
'''
