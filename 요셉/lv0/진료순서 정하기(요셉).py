def solution(emergency):
    emergency_ = sorted(emergency, reverse = True)
    answer = []
    for i in emergency:
        answer.append(emergency_.index(i)+1)
    return answer