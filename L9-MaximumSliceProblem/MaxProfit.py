# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A):
    # write your code in Python 3.6
    if len(A) < 2:
        return 0
    max_profit = [0] * len(A)
    max_profit[1] = A[1] - A[0]

    for i in range(2, len(A)):
        adjacent_max = A[i] - A[i - 1]
        curr_max = max(adjacent_max, max_profit[i - 1] + adjacent_max)
        max_profit[i] = curr_max

    max_possible_profit = max(max_profit)

    if max_possible_profit < 0:
        return 0
    else:
        return max_possible_profit
