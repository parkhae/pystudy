def solution(rank, attendance):
    answer = []
    answer_ ={}
    for i, j in enumerate(rank):
        answer_[j] = i
    for i in range(1,len(rank)+1):
        if attendance[answer_[i]] == True:
            answer.append(answer_[i])
    return answer[0]*10000+100*answer[1]+answer[2]