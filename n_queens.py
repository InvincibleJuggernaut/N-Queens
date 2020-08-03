n=int(input("Enter the size of the board"))

def reset():
    global board
    board=[[0]*n for i in range(8)]

reset()

def check(board, row, column):
    for i in range(0, column):
        if(board[row][i]==1):
            return False
    for i, j in zip(range(row, -1, -1), range(column, -1, -1)):
        if(board[i][j]==1):
            return False
    for i, j in zip(range(row, n), range(column, -1, -1)):
        if(board[i][j]==1):
            return False
    return True
    
def marker(board, column):
    if column>=n:
        return True
    for i in range(0, n):
        if(check(board, i, column)==True):
            board[i][column]=1
            if(marker(board, column+1)==True):
                return True
            board[i][column]=0
    return False

def display(board):
    if(marker(board, 0)==False):
        print("No feasible solutions exist")
    else:
        for i in range(0,n):
            for j in range(0,n):
                print(board[i][j])

display(board)
