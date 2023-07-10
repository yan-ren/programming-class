most=0
for i in list:
    biggest=0
    for j in i:
        count = 0
        if j == 1:
            count+=1
    if count>most:
        most=count
        biggest=list.index(i)
print([biggest,most])


mat = [[0,0,0],[0,1,1]]
index = 0

max_ones = 0
max_index = 0
while index < len(mat):
    if sum(mat[index]) > max_ones:
        max_ones = sum(mat[index])
        max_index = index

    index += 1

print([max_index, max_ones])

'''
Loop through each lists, for each list, count how many 1s inside and find the list with most 1s
'''
mat = [[0,0,0],[0,1,1]]

# def count_one(l):
#     count = 0
#     for value in l:
#         if value == 1:
#             count += 1
#     return count


index = 0
max_index = 0
max_ones = 0
while index < len(mat):
    # count number of ones
    number_of_ones = sum(mat[index])
    if number_of_ones > max_ones:
        max_ones = number_of_ones
        max_index = index

    index += 1

print([max_index, max_ones])



def row_with_max_ones(mat):
    # loop through each sub-list
    index = 0
    result = [0, 0]
    while index < len(mat):
        if sum(mat[index]) > result[1]:
            result = [index, sum(mat[index])]

        index += 1

    return result








































