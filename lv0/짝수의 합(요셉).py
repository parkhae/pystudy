def solution(n):
    answer = 0
    for i in range(n+1) :
        if i == int(i/2)*2 :
            answer += i
    return answer