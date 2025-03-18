def solution(n):
    answer = []
    while n != 1:
        i = 2
        while int(n/i) != n/i:
            i += 1
        n = n/i
        if i not in answer:
            answer.append(i)
    return answer