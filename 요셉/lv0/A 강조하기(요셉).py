def solution(myString):
    answer = ''
    for i in myString:
        if i in "Aa":
            answer += "A"
        else: answer += i.lower()
    return answer