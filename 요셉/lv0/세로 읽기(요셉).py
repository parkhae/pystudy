def solution(my_string, m, c):
    answer = ''
    word = []
    for i in range(0,len(my_string), m):
        word.append(my_string[i:i+m])
    for i in range(len(word)):
        answer += word[i][c-1]
    return answer