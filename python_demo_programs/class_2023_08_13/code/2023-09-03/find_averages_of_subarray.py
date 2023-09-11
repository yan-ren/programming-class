# first idea
def average_of_k(sample, k):
    temp = sample[:k]
    result = [sum(temp)/k]
    for i in range(k, len(sample)):
        temp = temp[1:k] + [sample[i]]
        result.append(sum(temp)/k)

    return result

def average_of_k_2(nums, k):
    output = []
    index = 0
    while index < len(nums):
        n = nums[index:index+1]
        if len(n) == k:
            output.append(sum(n) / len(n))
        index += 1
    return output


# idea: sliding window, O(N)
def find_averages_of_subarray(K, arr):
    result = []
    window_sum, window_start = 0, 0
    for i in range(len(arr)):
        window_sum += arr[i]
        if i >= K - 1:
            result.append(window_sum / K)
            window_sum -= arr[window_start]
            window_start += 1

    return result