def solution(arr):
    two = []
    for i in range(len(arr)):
        if arr[i] == 2:
            two.append(i)
    if len(two) == 0:
        print(two)
        return [-1]
    else:
        return arr[min(two):max(two)+1]