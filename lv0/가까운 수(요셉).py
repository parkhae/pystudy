def solution(array, n):
    answer = [sorted(array)[0], abs(n-sorted(array)[0])]
    for i in sorted(array):
        if answer[1] > abs(n-i):
            answer[0] = i
            answer[1] = abs(n-i)
    return answer[0]