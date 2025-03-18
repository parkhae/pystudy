def solution(array):
    answer = []
    answer_ = []
    dit = {}
    lst = sorted(tuple(array))
    for i in lst:
        dit[i] = array.count(i)
    for i in dit.keys():
        answer.append(i)
        answer_.append(dit[i])
    if answer_.count(max(answer_)) > 1:
        return -1
    else:
        return answer[answer_.index(max(answer_))]
    return 0