def solution(dots):
    xmin = 99999
    ymin = 99999
    xmax = -99999
    ymax = -99999
    for a in dots:
        i, j = a
        if i > xmax:
            xmax = i
        if i < xmin:
            xmin = i
        if j > ymax:
            ymax = j
        if j < ymin:
            ymin = j
    print(xmin, ymin, xmax, ymax)
    return (xmax-xmin)*(ymax-ymin)