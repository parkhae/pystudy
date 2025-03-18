def solution(todo_list, finished):
    answer = []
    for i in range(len(todo_list)):
        print(i)
        if finished[i] != True:
            answer.append(todo_list[i])
    return answer