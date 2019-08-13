# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(H):
    # write your code in Python 3.6
    stack = []
    count = 0
    for elem in H:
        if len(stack) == 0 or stack[len(stack) - 1] < elem:
            stack.append(elem)
        elif stack[len(stack) - 1] == elem:
            continue
        else:
            while len(stack) > 0:
                if stack[len(stack) - 1] > elem:
                    stack.pop()
                    count += 1
                    if len(stack) == 0:
                        stack.append(elem)
                        break
                elif stack[len(stack) - 1] == elem:
                    break
                else:
                    stack.append(elem)
                    break

    count += len(stack)

    return count


print(solution([8, 8, 5, 7, 9, 8, 7, 4, 8]))