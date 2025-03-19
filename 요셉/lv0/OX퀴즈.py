def solution(quiz):
    answer = []
    answer_ = []
    for i in quiz:
        answer_.append(i.split(' '))
    for i in range(len(answer_)):
        if answer_[i][1] == '+':
            if int(answer_[i][0]) + int(answer_[i][2]) == int(answer_[i][-1]):
                answer.append('O')
            else: answer.append('X')
        else:
            if int(answer_[i][0]) - int(answer_[i][2]) == int(answer_[i][-1]):
                answer.append('O')
            else: answer.append('X')
    return answer