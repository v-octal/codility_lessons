# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A, B):
    # write your code in Python 3.6
    stack = []
    q = 0

    while q < len(A):
        if len(stack) == 0:
            stack.append(q)
        else:
            did_q_win = True
            while len(stack) > 0 and B[stack[len(stack) - 1]] > B[q]:
                p = stack.pop()
                if A[p] > A[q]:
                    stack.append(p)
                    did_q_win = False
                    break

            if did_q_win:
                stack.append(q)

        q += 1

    return len(stack)


print(solution([4, 3], [1, 0]))
