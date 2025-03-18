def solution(str_list):
    for i, j in enumerate(str_list):
        if j == 'l':
            answer = str_list[:i]
            return answer
        elif j == 'r':
            answer = str_list[i+1:]
            return answer
    return []