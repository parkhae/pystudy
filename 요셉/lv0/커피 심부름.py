def solution(order):
    answer = 0
    for i in order:
        if 'ame' in i:
            answer += 4500
        elif 'latte' in i:
            answer += 5000
        else: answer += 4500
    return answer