def solution(myStr):
    answer = []
    for i in ['a', 'b', 'c']:
        myStr = myStr.replace(i, ' ')
    for i in myStr.split(' '):
        if len(i) > 0:
            answer.append(i)
    if len(answer) == 0:
        return ['EMPTY']
    return answer