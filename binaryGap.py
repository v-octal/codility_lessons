# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    bin = ""
    while N > 0:
        remainder = int(N % 2)
        bin += str(remainder)
        N = int(N/2)

    bin = bin[::-1]
    count = 0
    max = 0
    for val in bin:
        if val == '1':
            if count > max:
                max = count
            count = 0
        elif val == '0':
            count += 1
    return max
