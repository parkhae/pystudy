def solution(picture, k):
    answer = []
    for i in picture:
        stl = ''
        for j in i:
            stl += j*k
        for j in range(k):
            answer.append(stl)
    return answer