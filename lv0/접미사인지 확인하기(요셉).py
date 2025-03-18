def solution(my_string, is_suffix):
    back = []
    for i in range(len(my_string)):
        back.append(my_string[i::])
    if is_suffix in back:
        return 1
    else: return 0