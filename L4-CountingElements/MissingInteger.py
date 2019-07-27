# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    map = {}
    for elem in A:
        if elem > 0:
            map[elem] = True

    i = 1
    while i <= len(map):
        if i not in map:
            return i
        i += 1

    return len(map) + 1
