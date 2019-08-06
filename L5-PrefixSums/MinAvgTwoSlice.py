# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A):
    # write your code in Python 3.6
    curr_sum = (A[0] + A[1])
    i = 2
    curr_slice_start = 0
    min_avg = [curr_sum/2, curr_slice_start]

    while i < len(A):
        curr_sum += A[i]
        curr_sum_avg = curr_sum/(i - curr_slice_start + 1)
        prev_two_slice_sum = A[i - 1] + A[i]
        prev_two_slice_avg = prev_two_slice_sum/2

        if curr_sum_avg > prev_two_slice_avg:
            curr_sum = prev_two_slice_sum
            curr_slice_start = i - 1
            if min_avg[0] > prev_two_slice_avg:
                min_avg = [prev_two_slice_avg, curr_slice_start]
        else:
            if min_avg[0] > curr_sum_avg:
                min_avg = [curr_sum_avg, curr_slice_start]

        i += 1

    return min_avg[1]


print(solution([-3, -5, -8, -4, -10]))
