# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A):
    # write your code in Python 3.6
    val_map = {}
    front_leader = []
    reverse_leader = []
    curr_max = [A[0], 1]
    count = 0

    for i in range(len(A)):
        if A[i] in val_map:
            val_map[A[i]] += 1
            if val_map[A[i]] > curr_max[1]:
                curr_max = [A[i], val_map[A[i]]]
        else:
            val_map[A[i]] = 1

        if curr_max[1] > (i + 1)/2:
            front_leader.append(curr_max[0])
        else:
            front_leader.append(float('inf'))

    A.reverse()
    val_map = {}
    curr_max = [A[0], 1]

    for i in range(len(A)):
        if A[i] in val_map:
            val_map[A[i]] += 1
            if val_map[A[i]] > curr_max[1]:
                curr_max = [A[i], val_map[A[i]]]
        else:
            val_map[A[i]] = 1

        if curr_max[1] > (i + 1) / 2:
            reverse_leader.append(curr_max[0])
        else:
            reverse_leader.append(float('inf'))

    reverse_leader.reverse()

    for i in range(0, len(front_leader) - 1):
        if front_leader[i] != float('inf') and front_leader[i] == reverse_leader[i + 1]:
            count += 1

    return count

