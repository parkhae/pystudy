def solution(strArr):
    return [i.upper() if n%2 else i.lower() for n, i in enumerate(strArr)]
