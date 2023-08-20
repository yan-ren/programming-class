# ans = []
# # list1 = ["bella","label","roller"]
# list1 = ["cool","lock","cook"]
# for char in list1[0]:
#     ans.append(char)
# list1.remove(list1[0])

# for i in list1:
#     for char in ans:
#         if char in i:
#             i = i[:i.index(char)] + i[i.index(char) +1:]
#             continue
#         elif char not in i:
#             ans.remove(char)

# print(ans)


'''
Given a list of positive numbers and a positive number ‘k’, 
find the maximum sum of any contiguous sub list of size ‘k’.

Input: [2, 1, 5, 1, 3, 2], k=3 
Output: 9
Explanation: sub list with maximum sum is [5, 1, 3].

Input: [2, 3, 4, 1, 5], k=2 
Output: 7
Explanation: sub list with maximum sum is [3, 4].
'''

def max_sub_list(k, list):
    if k > len(list):
        return -1
        
    max_sum = 0
    current_sum = 0
    start = 0

    for index in range(len(list)):
        current_sum += list[index]

        if index >= k - 1:
            max_sum = max(max_sum, current_sum)
            current_sum -= list[start]
            start += 1

    return max_sum


print(max_sub_list(3, [2, 1, 5, 1, 3, 2]))
