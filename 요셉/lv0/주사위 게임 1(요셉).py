def solution(a, b):
    if int(a/2) == a/2 and int(b/2) == b/2:
            return abs(a-b)
    elif int(a/2) != a/2 and int(b/2) != b/2:
        return a**2 + b**2
    else:
        return 2*(a+b)