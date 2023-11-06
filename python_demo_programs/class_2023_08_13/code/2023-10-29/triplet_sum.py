def triplet_sum(arr):
    arr.sort() # runtime O(N) = NlogN
    result = []
    for index in range(len(arr)):
        # skip same element to avoid duplicate triplets
        if index > 0 and arr[index] == arr[index-1]:
            continue
        two_sum(arr, -arr[index], index+1, result)

    return result


def two_sum(arr, target, start_index, result):
    right_index = len(arr) - 1
    left_index = start_index

    while left_index < right_index:
        current_sum = arr[left_index] + arr[right_index]
        if current_sum == target:
            result.append([-target, arr[left_index], arr[right_index]])
            left_index += 1
            right_index -= 1
            # skip the same element on the left pointer to avoid duplicate
            while left_index < right_index and arr[left_index] == arr[left_index-1]:
                left_index += 1
            # skip the same element on the right pointer to avoid duplicate
            while left_index < right_index and arr[right_index] == arr[right_index+1]:
                right_index -= 1
        elif target > current_sum:
            left_index += 1
        else:
            right_index -= 1


print(triplet_sum([-3, 0, 1, 2, -1, 1, -2]))