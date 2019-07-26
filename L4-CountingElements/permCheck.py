# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    numStatus = {}
    n = len(A)
    i = 1
    while i <= n:
        numStatus[i] = False
        i += 1

    for elem in A:
        if elem in numStatus:
            if numStatus[elem]:
                return 0
            numStatus[elem] = True
        else:
            return 0

    for key in numStatus:
        if not numStatus[key]:
            return 0

    return 1
