def solution(num_list):
    answer = 0
    for i in num_list:
        n = 0
        while i != 1:
            if i%2 == 0:
                i = i/2
                n += 1
            else:
                i = (i-1)/2
                n += 1
        answer += n
    return answer