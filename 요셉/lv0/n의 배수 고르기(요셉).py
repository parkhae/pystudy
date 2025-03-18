def solution(n, numlist):
    answer = []
    for i in numlist:
        if int(i/n) == i/n :
            answer.append(i)
    return answer