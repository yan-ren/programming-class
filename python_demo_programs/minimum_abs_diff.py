# def minimumAbsDifference(arr):
#     arr.sort()
#     # find the min difference
#     index = 0
#     min_diff = float("inf")
#     while index < len(arr) - 1:
#         if arr[index+1] - arr[index] < min_diff:
#             min_diff = arr[index+1] - arr[index]
#         index += 1

#     index = 0
#     res = []
#     while index < len(arr) - 1:
#         if arr[index + 1] - arr[index] == min_diff:
#             res.append([arr[index], arr[index+1]])
#         index += 1
#     return res

# print(minimumAbsDifference([4,2,1,3]))

def minimumAbsDifference(arr):
    arr.sort()
    min_difference = arr[1] - arr[0]
    index = 0
    while index < len(arr) - 1:
        if arr[index + 1] - arr[index] < min_difference:
            min_difference = arr[index+1] - arr[index]
        index+=1
    
    res = []
    index = 0
    while index < len(arr) - 1:
        if arr[index+1] - arr[index] == min_difference:
            res.append([arr[index], arr[index+1]])
        index += 1
    return res

print(minimumAbsDifference([4,2,1,3]))
print(minimumAbsDifference([1,3,6,10,15]))
print(minimumAbsDifference([3,8,-10,23,19,-4,-14,27]))