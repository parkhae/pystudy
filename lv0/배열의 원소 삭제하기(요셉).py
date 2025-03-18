def solution(arr, delete_list):
    for i in delete_list:
        if i in arr:
            j = arr.count(i)
            for k in range(j):
                arr.remove(i)
    return arr