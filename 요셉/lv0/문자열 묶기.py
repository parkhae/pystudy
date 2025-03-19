def solution(strArr):
    answer = 0
    answer_ = []
    for i in strArr:
        answer_.append(len(i))
    for j in range(31):
        if answer_.count(j) >= answer:
            answer = answer_.count(j) 
    return answer