def solution(numlist, n):
    answer = []
    answer_ = []
    answer__ = []
    dit = {}
    for i in numlist:
        dit[i] = abs(i-n)
    for i in sorted(dit.keys(), reverse = True):
        answer_.append(i)
        answer__.append(dit[i])
    while len(answer__) != 0:
        mins = min(answer__)
        idx = answer__.index(mins)
        answer.append(answer_[idx])
        answer__.pop(idx)
        answer_.pop(idx)
    return answer