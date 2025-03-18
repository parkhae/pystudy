def solution(numbers):
    num = sorted(numbers)
    max1 = num[0]*num[1]
    max2 = num[-1]*num[-2]
    if max1 > max2 :
        return max1
    return max2