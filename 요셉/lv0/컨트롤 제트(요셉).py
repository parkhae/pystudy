def solution(s):
    answer = 0
    s_ = s.split(' ')
    for i in range(len(s_)):
        if s_[i] == 'Z':
            answer -= int(s_[i-1])
        else:
            answer += int(s_[i])
    return answer