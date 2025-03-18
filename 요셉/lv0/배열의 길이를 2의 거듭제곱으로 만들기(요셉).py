def solution(arr):
    i = 1
    while 2**i < len(arr):
        if len(arr) > 2**i and len(arr) <= 2**(i+1):
            for j in range(2**(i+1) - len(arr)):
                arr.append(0)
            break
        else: i += 1
    return arr