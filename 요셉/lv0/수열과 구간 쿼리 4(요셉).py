def solution(arr, queries):
    for query in queries:
        a, b, c = query
        for i in range(len(arr)): 
            if a <= i and i <= b:
                if i % c == 0:
                    arr[i] += 1
    return arr