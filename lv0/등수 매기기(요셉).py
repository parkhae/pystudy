def solution(score):
    answer = []
    answer_ = []
    n = 1
    for i in range(len(score)):
        answer_.append((score[i][0]+score[i][1])/2)
        answer.append(0)
    for i, j in enumerate(sorted(set(answer_), reverse = True)):
        idx = [l for l, value in enumerate(answer_) if value == j]
        for k in idx:
            answer[k] = n
        print(n)
    return answer