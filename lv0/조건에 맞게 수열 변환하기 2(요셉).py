def solution(arr):
    answer = 0
    arr_ = []
    while arr != arr_:
        answer += 1
        arr_ = []
        for i in range(len(arr)):
            arr_.append(arr[i])
            if arr[i]%2 == 0 and arr[i] >= 50:
                arr[i] = arr[i]/2
            elif arr[i]%2 == 1 and arr[i] < 50:
                arr[i] = arr[i]*2 +1
    return answer -1