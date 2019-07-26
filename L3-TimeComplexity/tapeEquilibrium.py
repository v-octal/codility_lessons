# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    aSum = 0
    nthSum = []
    for elem in A:
        aSum += elem
        nthSum.append(aSum)

    nthSum.pop()
    runningSum = 0
    min = float("inf")

    for elem in nthSum:
        diff = abs((aSum - elem) - elem)
        if diff < min:
            min = diff

    return min
