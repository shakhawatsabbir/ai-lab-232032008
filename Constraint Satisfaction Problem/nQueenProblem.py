def isSafe(board, row, col, n):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solveNQUtil(board, col, n):
    if col >= n:
        return True
    for i in range(n):
        if isSafe(board, i, col, n):
            board[i][col] = 1
            if solveNQUtil(board, col + 1, n) == True:
                return True
            board[i][col] = 0 
    return False

def solveNQ(n):
    board = [[0] * n for _ in range(n)]

    if solveNQUtil(board, 0, n) == False:
        print("Solution does not exist")
        return False
    for i in board:
        print(i)
    return True

n = 4
solveNQ(n)