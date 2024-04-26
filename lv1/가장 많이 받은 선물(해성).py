def solution(friends, gifts):
    n = len(friends)
    result = [0] * n

    total_gift = [[0 for _ in range(n)] for _ in range(n)]

    friends = {f:i for i, f in enumerate(friends)}

    for g in gifts:
        total_gift[friends[g.split()[0]]][friends[g.split()[1]]] += 1
    gift_score = [sum(i) - sum(j) for i, j in zip(total_gift, list(zip(*total_gift)))]

    for i in range(n-1):
        for j in range(i+1,n):
            if total_gift[i][j] > total_gift[j][i]:
                result[i] += 1
            elif total_gift[i][j] < total_gift[j][i]:
                result[j] += 1
            else:
                if gift_score[i] > gift_score[j]:
                    result[i] += 1
                elif gift_score[i] < gift_score[j]:
                    result[j] += 1
    return max(result)
