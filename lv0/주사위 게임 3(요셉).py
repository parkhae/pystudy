def solution(a, b, c, d):
    answer = 0
    dice = [a, b, c, d]
    if dice.count(a) == 4:
        return a*1111
    elif len(set(dice)) == 4:
        return min(dice)
    elif dice.count(a) >= 2 or dice.count(b) >= 2 or dice.count(c) >= 2 or dice.count(d) >= 2:
        if len(set(dice)) == 3:
            for i in dice:
                if dice.count(i) == 2:
                    dice.remove(i)
                    dice.remove(i)
                    break
            print(dice)
            return dice[0]*dice[1]
        elif a == b and c == d:
            return (a+c)*abs(a-c)
        elif a == c and b == d:
            return (a+b)*abs(a-b)
        elif a == d and b == c:
            return (a+b)*abs(a-b)
        else:
            for i in dice:
                if dice.count(i) == 3:
                    dice.remove(i)
                    dice.remove(i)
                    dice.remove(i)
                    break
            return(10*i+dice[0])**2