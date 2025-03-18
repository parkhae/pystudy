def solution(common):
    answer = 0
    if common[2] == 2*common[1]-common[0]:
        return common[len(common)-1] + common[1]-common[0]
    else: return common[len(common)-1]*(common[len(common)-1]/common[len(common)-2])