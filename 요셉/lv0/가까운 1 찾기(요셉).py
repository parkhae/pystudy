def solution(arr, idx):
    for i in range(len(arr)):
        if i >= idx and arr[i] == 1:
            answer = i
            return answer
    return -1