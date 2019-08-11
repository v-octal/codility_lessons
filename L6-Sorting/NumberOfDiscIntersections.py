# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import bisect


def solution(A):
    # write your code in Python 3.6
    count = 0
    end_points = [(i - A[i], i + A[i]) for i in range(len(A))]
    end_points.sort()

    right_end_points = [elem[0] for elem in end_points]
    i = 0
    while i < len(end_points):
        if count > 10000000:
            return -1
        curr_intersecting_circle_count = bisect.bisect_right(right_end_points, end_points[i][1]) - 1

        count += curr_intersecting_circle_count - i

        i += 1

    return count

