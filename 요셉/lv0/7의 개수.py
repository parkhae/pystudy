def solution(array):
    answer = 0
    for i in array:
        j = str(i)
        for l in j:
            if int(l) == 7:
                answer += 1
    return answer