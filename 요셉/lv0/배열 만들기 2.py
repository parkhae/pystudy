def solution(l, r):
    answer = []
    list_ = [x for x in range(l,r+1)]
    for i in list_:
        if set([x for x in str(i)]) == {'5'} or set([x for x in str(i)]) == {'5', '0'} or 
set([x for x in str(i)]) == {'0'}:
            answer.append(i)
            
    if len(answer) != 0:
        return answer
    else : return [-1]