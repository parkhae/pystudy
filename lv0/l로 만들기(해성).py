def solution(myString):
    s = 'abcdefghijk'
    return ''.join('l' if i in s else i for i in myString)
