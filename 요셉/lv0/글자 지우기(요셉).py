def solution(my_string, indices):
    my_string = list(my_string)
    for i in sorted(indices, reverse = True):
        my_string.pop(i)
    return ''.join(my_string)