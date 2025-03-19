def solution(myString, pat):
    for i in range(len(pat), len(myString)+1):
        if pat == myString[i-len(pat):i]:
            print(myString[i-len(pat):i])
            answer = myString[:i]
    return answer