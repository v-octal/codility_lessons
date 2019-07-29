# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    zeroCount = 0
    oneCount = 0
    passingCars = 0

    for elem in A:
        if elem == 1:
            passingCars += zeroCount
            oneCount += 1
        elif elem == 0:
            zeroCount += 1

        if passingCars > 1000000000:
            return -1

    return passingCars
