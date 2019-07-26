# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, A):
    # write your code in Python 3.6
    i = 1
    path = {}
    while i <= X:
        path[i] = False
        i += 1

    i = 0
    while i < len(A):
        if A[i] in path:
            path.pop(A[i])
            if len(path) == 0:
                return i
        i += 1

    return -1
