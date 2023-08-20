def min_abs_difference(arr):
    arr.sort()
    # [1, 2, 3, 4]
    min_diffrence = float("inf")
    for i in range(len(arr) - 1):
        if arr[i+1] - arr[i] < min_diffrence:
            min_diffrence = arr[i+1] - arr[i]

    answer = []
    for i in range(len(arr)  - 1):
        if arr[i + 1] - arr[i] == min_diffrence:
            answer.append([arr[i], arr[i+1]])

    return answer


def unique_occurrances(arr):
    s = set()

    for i in arr:
        if i in s:
            return False
        else:
            s.add(i)

    return True

