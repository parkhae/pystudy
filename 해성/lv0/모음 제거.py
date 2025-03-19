def solution(my_string):
    answer = ''
    return ''.join(i for i in my_string if i not in 'aeiou')
