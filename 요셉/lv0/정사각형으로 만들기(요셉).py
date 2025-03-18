def solution(arr):
    answer = answer = [[0 for x in range(max([len(arr), len(arr[0])]))] for x in range(max([len(arr), len(arr[0])]))]
    if len(arr) > len(arr[0]):
        for i in range(max([len(arr), len(arr[0])])):
            for j in range(min([len(arr), len(arr[0])])):
                answer[i][j] = arr[i][j]
    else:
        for i in range(min([len(arr), len(arr[0])])):
            for j in range(max([len(arr), len(arr[0])])):
                answer[i][j] = arr[i][j]   
    return answer