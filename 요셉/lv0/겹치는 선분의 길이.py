def solution(lines):
    feature = []
    answer = 0 
    
    for i in range(len(lines)):
        for j in range(lines[i][0],lines[i][1]):
            print(j)
            feature.append(j)

    max_ = max(feature)
    min_ = min(feature)
    for i in range(min_,max_+1):
        if feature.count(i) > 1:
            answer += 1
    
    return answer