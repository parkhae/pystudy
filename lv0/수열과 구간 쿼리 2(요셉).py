def solution(arr, queries):
    answer = []
    for i in queries:
        answer_ = []
        a, b, c = i
        for j in sorted(arr[a:b+1]):
            if j > c:
                answer_.append(j)
                break
        if len(answer_) != 1:
            answer_.append(-1)
        answer.append(answer_[0])
    return answer