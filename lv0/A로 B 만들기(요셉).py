def solution(before, after):
    bfd = {}
    afd = {}
    for i in before:
        bfd[i] = 0
    for i in after:
        afd[i] = 0
        
    for j in before:
        bfd[j] += 1
    for j in after:
        afd[j] += 1
        
    if bfd == afd:
        return 1
    else:
        return 0