def solution(num_list):
    answer = []
    for i in range(0,5):
        answer.append(sorted(num_list)[i])
    return answer