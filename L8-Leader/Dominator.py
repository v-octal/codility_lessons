# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A):
    # write your code in Python 3.6
    if len(A) == 1:
        return 0
    val_map = {}
    for i in range(len(A)):
        if A[i] in val_map:
            val_map[A[i]] += 1
            if val_map[A[i]] > len(A)/2:
                return i
        else:
            val_map[A[i]] = 1

    return -1
