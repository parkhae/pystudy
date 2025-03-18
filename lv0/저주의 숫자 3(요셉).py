def solution(n):
    answer = 0
    for i in range(1, n*10):
        if i%3 != 0 and str(3) not in str(i):
            answer += 1
        if answer == n:
            return i