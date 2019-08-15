# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A):
    # write your code in Python 3.6
    max_slice = [0] * len(A)
    max_slice[0] = A[0]

    for i in range(1, len(A)):
        max_slice[i] = max(A[i], max_slice[i - 1] + A[i])

    return max(max_slice)
