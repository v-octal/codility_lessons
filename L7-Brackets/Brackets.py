# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(S):
    # write your code in Python 3.6
    stack = []
    openings = ['(', '{', '[']
    closings = [')', '}', ']']

    for ch in S:
        if ch in openings:
            stack.append(ch)
        elif len(stack) == 0:
            return 0
        elif ch in closings:
            pos = closings.index(ch)
            if stack.pop() != openings[pos]:
                return 0

    if len(stack) != 0:
        return 0

    return 1

