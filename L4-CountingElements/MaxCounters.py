# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, A):
    counters = [0] * N

    maxVal = 0
    setAll = 0
    for elem in A:
        if elem == N + 1:
            setAll = maxVal
        else:
            counters[elem - 1] = max(setAll, counters[elem - 1])
            counters[elem - 1] += 1
            if counters[elem - 1] > maxVal:
                maxVal = counters[elem - 1]

    for i in range(len(counters)):
        counters[i] = max(counters[i], setAll)
    return counters
