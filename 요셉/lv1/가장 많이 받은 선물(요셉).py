def solution(friends, gifts):
    import numpy as np
    mat = np.zeros((len(friends),len(friends)))
    gift_index = np.zeros((2, len(friends)))
    
    for i in gifts :
        a, b = i.split(' ')
        mat[friends.index(a)][friends.index(b)] += 1
        
    for i in range(len(friends)):
        for j in range(len(friends)):
            gift_index[0][i] +=  mat[i][j]-mat[j][i]
            
    for i in range(len(friends)) :
        for j in range(i+1):
            if i != j:
                if mat[i][j] > mat[j][i] :
                    gift_index[1][i] += 1
                elif  mat[i][j] == mat[j][i] :
                    if gift_index[0][i] > gift_index[0][j]:
                        gift_index[1][i] += 1
                    elif gift_index[0][i] < gift_index[0][j]:
                        gift_index[1][j] += 1
                else : gift_index[1][j] += 1
                    
    answer = max(gift_index[1][:])

    return answer