def solution(num, total):
    for i in range(-1000,1000):
        if i*num+sum([x for x in range(num)]) == total:
            return [i+x for x in range(num)]