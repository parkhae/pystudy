def solution(my_str, n):
    answer = []
    i = 0
    a, b = divmod(len(my_str), n)
    for j in range(a):
        answer.append(my_str[i:n*(j+1)])
        i = n*(j+1)
    if b != 0:
        answer.append(my_str[i:a*n+b])
    return answer