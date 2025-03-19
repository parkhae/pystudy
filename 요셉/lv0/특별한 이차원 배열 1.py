def solution(n):
    box1 = []
    box2 = []
    for i in range(n):
        for j in range(n):
            box1.append(0)
        box2.append(box1)
        box1 = []
        
    for i in range(n):
        box2[i][i] = 1
    
    return box2