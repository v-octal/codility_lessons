# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    # write your code in Python 3.6
    if len(A) <= 1:
        return A
    if K == len(A) or K == 0:
        return A
    if K > len(A):
        K = K % len(A)
    result = []
    looped = False
    i = len(A) - K
    while True:
        result.append(A[i])
        i += 1
        if i == len(A):
            i = 0
            looped = True
        if looped and i == len(A) - K:
            break

    return result
