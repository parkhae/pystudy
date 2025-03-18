def solution(n):
    for i in range(6,6*100+1,6):
        if i/n == int(i/n):
            return i/6