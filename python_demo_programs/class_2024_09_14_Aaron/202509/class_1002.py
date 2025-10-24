'''
Given a list of pairs [[1, 2], [3, 2], [4, 5]] find which pair has the largest sum
'''
def max_pair(matrix):
    # loop through each pair, calculate the sum, compare find the largest
    # save the pair for the largest, return it
    max_pair = [0, 0]

    for pair in matrix:
        if pair[0] + pair[1] > max_pair[0] + max_pair[1]:
            max_pair = pair

    return max_pair

print(max_pair([[1, 2], [3, 2], [4, 5]]))

'''follow up
if the number of value in pair is not fixed

Given a list of pairs [[1, 2, 2], [3, 2], [9]] find which pair has the largest sum

need additional feature that can calculate the sum given a list
'''