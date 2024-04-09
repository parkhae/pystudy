def solution(myString, pat):
    return int(pat.translate(str.maketrans("AB","BA")) in myString)
