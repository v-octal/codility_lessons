# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    num = {}
    for elem in A:
        if elem in num:
            num[elem] += 1
        else:
            num[elem] = 1

    result = []
    for key in num:
        if num[key] % 2 != 0:
            result.append(key)

    return result[0]
