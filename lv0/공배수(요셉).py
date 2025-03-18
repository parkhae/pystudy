def solution(number, n, m):
    if number/n == int(number/n) and number/m == int(number/m):
        return 1
    else: return 0