def solution(n):
    answer = 0
    facto = 1
    for i in range(1,n+1):
        if facto*i < n:
            facto = facto*i
            answer += 1
        elif facto * i == n:
            return answer + 1
        else:
            return answer