def solution(bin1, bin2):
    lst = [0 for x in range(max([len(bin1), len(bin2)]))]
    for i, j in enumerate(bin1[::-1]):
        lst[i] += int(j)
    for i, j in enumerate(bin2[::-1]):
        lst[i] += int(j)
        
    for i, j in enumerate(lst):
        a, b = divmod(j,2)
        if a >= 1 and i+1 < len(lst):
            lst[i+1] += a
        elif a >= 1 and i+1 >= len(lst):
            lst.append(a)
        lst[i] = b

    return ''.join([str(x) for x in lst])[::-1]