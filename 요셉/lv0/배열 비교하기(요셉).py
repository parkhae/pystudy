def solution(arr, n):
    answer = []
    if len(arr)/2 == int(len(arr)/2):
        for i in range(len(arr)):
            if i/2 == int(i/2):
                answer.append(arr[i])
            else: answer.append(arr[i]+n)
    else:
        for i in range(len(arr)):
            if i/2 == int(i/2):
                answer.append(arr[i]+n)
            else: answer.append(arr[i])
    return answer