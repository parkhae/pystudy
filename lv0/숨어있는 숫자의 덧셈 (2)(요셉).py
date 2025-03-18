def solution(my_string):
    answer = 0
    low = 'abcdefghijklmnopqrstuvwxyz'
    up = low.upper()
    for i in low:
        if i in my_string:
            my_string = my_string.replace(i,' ')
    for j in up.upper():
        if j in my_string:
            my_string = my_string.replace(j,' ')
    answer_ = my_string.split(' ')
    for i in answer_:
        if i != '':
            answer += int(i)
    return answer