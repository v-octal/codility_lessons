# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A):
    if len(A) < 4:
        return 0
    forward_max_slice = [0] * len(A)
    forward_max_slice[0] = 0

    for i in range(1, len(A)):
        forward_max_slice[i] = max(A[i], forward_max_slice[i - 1] + A[i])

    backward_max_slice = [0] * len(A)
    backward_max_slice[len(A) - 1] = 0

    for i in range(len(A) - 2, -1, -1):
        backward_max_slice[i] = max(A[i], backward_max_slice[i + 1] + A[i])

    max_double_slice = -float('inf')

    for i in range(1, len(A) - 1):
        curr_double_slice = forward_max_slice[i - 1] + backward_max_slice[i + 1]
        if curr_double_slice > max_double_slice:
            max_double_slice = curr_double_slice
        if forward_max_slice[i - 1] > max_double_slice:
            max_double_slice = forward_max_slice[i - 1]
        if backward_max_slice[i + 1] > max_double_slice:
            max_double_slice = backward_max_slice[i + 1]

    if max_double_slice < 0:
        return 0

    return max_double_slice


print(solution([0, 10, -5, -2, 0]))
