# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A, B, K):
    # write your code in Python 3.6
    i = A
    while i <= B:
        if i % K == 0:
            break

        i += 1

    if i > B:
        return 0

    return int((B - i)/K) + 1

