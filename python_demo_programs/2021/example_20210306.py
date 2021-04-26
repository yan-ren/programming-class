x = 2
x = 3

def foo():
    global s  # tell foo() uses global s
    print(s)
    s = "That's clear" # define local s ? change the global s
    print(s) # print global s
    x = 20
    print(globals())
    print(locals())


s = "Python" # set a global s
foo()
print(s)

def sortedSquares(nums):
    index = 0
    while index < len(nums):
        nums[index] = nums[index] ** 2
    nums.sorted()
