# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
def binaryCheck(array, low, high):
    if len(array) == 0:
        return False
    start = 0
    end = len(array) - 1
    if array[start] > high or array[end] < low:
          return False
    while start < end:
        mid = int((start+end)/2)
        if array[mid] >= low and array[mid] <= high:
            return True
        elif array[mid] < low:
            start = mid + 1
        elif array[mid] > high:
            end = mid - 1

    if start == end:
        if array[start] >= low and array[start] <= high:
            return True

    return False


def solution(S, P, Q):
    # write your code in Python 3.6
    a = []
    c = []
    g = []
    t = []

    i = 0

    while i < len(S):
        if S[i] == 'A':
            a.append(i)
        elif S[i] == 'C':
            c.append(i)
        elif S[i] == 'G':
            g.append(i)
        elif S[i] == 'T':
            t.append(i)

        i += 1

    i = 0
    ans = []
    while i < len(P):
        if binaryCheck(a, P[i], Q[i]):
            ans.append(1)
        elif binaryCheck(c, P[i], Q[i]):
            ans.append(2)
        elif binaryCheck(g, P[i], Q[i]):
            ans.append(3)
        elif binaryCheck(t, P[i], Q[i]):
            ans.append(4)
        else:
            print('X')

        i += 1

    return ans

print(solution('C', [0], [0]) )
