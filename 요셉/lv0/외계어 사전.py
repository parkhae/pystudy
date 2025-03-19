def solution(spell, dic):
    for i in dic:
        for j in spell:
            if j in i:
                answer = True
            else:
                answer = False
                break
        if answer:
            return 1
    return 2