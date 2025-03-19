def solution(arr):
    for n, i in enumerate(arr):
        if i%2==0 and i>=50:
            arr[n] = i/2
        elif i%2 and i<50:
            arr[n] = i*2
    return arr
