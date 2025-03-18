def solution(myString, pat):
    mystr = ""
    for i in myString:
        if i == "A":
            mystr += "B"
        else: mystr += "A"
    if pat in mystr:
        return 1
    else: return 0