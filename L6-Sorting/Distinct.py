# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A):
    # write your code in Python 3.6
    distinct = {}

    for elem in A:
        if elem not in distinct:
            distinct[elem] = True

    return len(distinct)

