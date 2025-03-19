def solution(my_string):
    ans = my_string.split()
    answer = int(ans[0])
    for i in range(2, len(ans),2):
        if ans[i-1] == '+':
            answer += int(ans[i])
        else: answer -= int(ans[i])
    return answer