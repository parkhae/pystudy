def solution(sides):
    answer = 0
    for i in range(1,max(sides)):
        if i <= max(sides) and i+min(sides) > max(sides):
            print(i)
            answer += 1
    for i in range(1,sum(sides)):
        if i >= max(sides):
            answer += 1
    return answer