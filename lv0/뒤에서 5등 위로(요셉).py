def solution(num_list):
    answer = []
    for i in range(5,len(num_list)):
        answer.append(sorted(num_list)[i])
    return answer