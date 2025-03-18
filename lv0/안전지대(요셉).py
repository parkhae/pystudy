def solution(board):
    answer = 0
    board_ = [[0 for _ in range(len(board[0])+2)] for _ in range(len(board)+2)]
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 1:
                board_[i+1][j+1] += 1
                board_[i+1][j] += 1
                board_[i+1][j+2] += 1
                board_[i][j] += 1
                board_[i][j+1] += 1
                board_[i][j+2] += 1
                board_[i+2][j+2] += 1
                board_[i+2][j+1] += 1
                board_[i+2][j] +=1
                
    for i in range(1,len(board_)-1):
        for j in range(1,len(board_[i])-1):
            if board_[i][j] == 0:
                answer += 1
    return answer