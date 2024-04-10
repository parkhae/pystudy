def solution(array, height):
    answer = 0
    for i in sorted(array):
        if i > height:
            answer+= 1
    return answer