def solution(A, B):
    if A == B:
        return 0
    for i in range(0,len(A)):
        if A[-i:]+A[:-i] == B:
            return i
    return -1