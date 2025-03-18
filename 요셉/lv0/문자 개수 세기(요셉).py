def solution(my_string):
    answer = []
    for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz':
        answer.append(my_string.count(i))
    return answer