def solution(num_list):
    x, y = 0, 0
    for i in num_list:
        y += i%2
        x += (i+1)%2
    return [x,y]
