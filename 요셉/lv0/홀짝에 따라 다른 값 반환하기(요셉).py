def solution(n):
    answer = 0
    if int(n/2) == n/2:
        for i in range(1, n+1):
            if int(i/2) == i/2:
                answer += i**2
    else:
        for i in range(1, n+1):
            if int(i/2) != i/2:
                answer += i
    return answer