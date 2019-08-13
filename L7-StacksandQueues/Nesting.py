# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(S):
    # write your code in Python 3.6
    stack = []

    for ch in S:
        if ch == '(':
            stack.append(ch)
        elif len(stack) == 0:
            return 0
        else:
            if stack.pop() != '(':
                return 0

    if len(stack) != 0:
        return 0

    return 1

