def solution(n):
    answer = [[1 for x in range(n)] for x in range(n)]
    answer_ = [[n-1,n-1]]
    for i in range(n):
        if answer_[i][1] == 0:
            break
        if answer_[i][1] > 0:
            answer_.append([-answer_[i][1],-answer_[i][1]+1])
        else:
            answer_.append([-answer_[i][1], -answer_[i][1]-1])
    a = 0
    b = 0
    m = 1
    for i in range(len(answer_)):
        if answer_[i][0] > 0:
            for j in range(answer_[i][0]+1):
                if j == 0:
                    pass
                else:
                    b += 1
                    m += 1
                    answer[a][b] = m
        else:
            for j in range(answer_[i][0],0):
                if j == 0:
                    pass
                else:
                    b -= 1
                    m += 1
                    answer[a][b] = m
        if answer_[i][1] > 0:
            for j in range(answer_[i][1]+1):
                if j == 0:
                    pass
                else:
                    a += 1
                    m += 1
                    answer[a][b] = m
        else:
            for j in range(answer_[i][1],0):
                if j == 0:
                    pass
                else:
                    a -= 1
                    m += 1
                    answer[a][b] = m
    return answer