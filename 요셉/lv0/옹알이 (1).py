def solution(babbling):
    answer = 0
    talk = ['aya', 'ye', 'woo', 'ma']
    for i in babbling:
        for j in talk:
            if j in i:
                i = i.replace(j,' ')
        if len(i.replace(' ','')) == 0:
            answer += 1
    return answer