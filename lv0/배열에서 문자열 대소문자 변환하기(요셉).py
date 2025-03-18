def solution(strArr):
    answer = []
    for i in range(len(strArr)):
        if i/2 == int(i/2):
            answer.append(strArr[i].lower())
        else: answer.append(strArr[i].upper())
    return answer