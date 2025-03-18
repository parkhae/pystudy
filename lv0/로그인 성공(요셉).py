def solution(id_pw, db):
    answer = ''
    if id_pw in db:
        return 'login'
    for i, j in db:
        if i == id_pw[0] and j != id_pw[1]:
            return 'wrong pw'
    return 'fail'