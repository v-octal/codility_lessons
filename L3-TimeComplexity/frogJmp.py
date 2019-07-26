import math
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, Y, D):
    # write your code in Python 3.6

    return math.ceil((Y-X)/D)

print(solution(1, 5, 2))
