# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A):
    # write your code in Python 3.6
    max_nums = [-float('inf')] * 3
    neg_nums = [float('inf')] * 2

    i = 0

    while i < len(A):
        if A[i] > max_nums[0]:
            max_nums[2] = max_nums[1]
            max_nums[1] = max_nums[0]
            max_nums[0] = A[i]
        elif A[i] > max_nums[1]:
            max_nums[2] = max_nums[1]
            max_nums[1] = A[i]
        elif A[i] > max_nums[2]:
            max_nums[2] = A[i]

        if A[i] < 0 and A[i] < neg_nums[0]:
            neg_nums[1] = neg_nums[0]
            neg_nums[0] = A[i]
        elif A[i] < 0 and A[i] < neg_nums[1]:
            neg_nums[1] = A[i]

        i += 1

    if float('inf') in neg_nums:
        return max_nums[0] * max_nums[1] * max_nums[2]

    if max_nums[0] < 0:
        return max_nums[0] * max_nums[1] * max_nums[2]
    elif max_nums[1] < 0:
        return max_nums[0] * neg_nums[0] * neg_nums[1]
    elif max_nums[1] < abs(neg_nums[0]):
        return max_nums[0] * neg_nums[0] * neg_nums[1]
    else:
        return max_nums[0] * max_nums[1] * max_nums[2]


