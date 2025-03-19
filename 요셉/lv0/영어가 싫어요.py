def solution(numbers):
    answer = ''.join(numbers)
    floats = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9, 'zero':0}
    for i in floats.keys():
        if i in answer:
            answer = answer.replace(i,str(floats[i]))
    return int(answer)