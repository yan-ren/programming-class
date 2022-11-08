import queue


def moving_average(l, N):
    q = queue.Queue()
    sum = 0
    result = []
    for i in l:
        q.put(i)
        sum += i
        if q.qsize() == N:
            result.append(sum / N)
            sum -= q.get()

    return result


print(moving_average([2, 3, 1, 4, 6, 1, 2], 3))
# [2, 8/3, 11/3, 11/3, 3]
