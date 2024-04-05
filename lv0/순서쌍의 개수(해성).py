def solution(n):
    return [n%i for i in list(range(1,n+1))].count(0)
