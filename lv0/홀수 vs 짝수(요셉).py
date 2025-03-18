def solution(num_list):
    sum1 = 0
    sum2 = 0
    for i in range(len(num_list)):
        if i/2 == int(i/2):
            sum1 += num_list[i]
        else: sum2 += num_list[i]
        
    if sum1 > sum2:
        return sum1
    elif sum1 < sum2:
        return sum2
    else: return sum1