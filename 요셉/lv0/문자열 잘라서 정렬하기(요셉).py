def solution(myString):
    answer = []
    string = myString.split('x')
    for i in string:
        if i != '':
            answer.append(i)
    return sorted(answer)