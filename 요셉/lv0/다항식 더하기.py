def solution(polynomial):
    poly = polynomial.split(' ')
    coef = 0
    cons = 0
    for i in range(0, len(poly),2):
        if 'x' in poly[i]:
            if poly[i][0] == 'x':
                coef += 1
            else:
                coef += int(poly[i][:-1])
        else:
            cons += int(poly[i])
    if coef == 1:
        if cons == 0:
            return 'x'
        else: return f'x + {cons}'
    elif coef == 0:
        if cons != 0:
            return f'{cons}'
        else:
            return ''
    else:
        if cons == 0:
            return f'{coef}x'
        else:
            return f'{coef}x + {cons}'