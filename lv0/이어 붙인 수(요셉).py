def solution(num_list):
    hol = ''
    jjag = ''
    for i in num_list:
        if int(i/2) == i/2:
            hol += str(i)
        else:
            jjag += str(i)
    return int(hol) + int(jjag)