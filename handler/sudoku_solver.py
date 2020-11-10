res = []

def backtracksudoku(board):
    empty_pos = find_empty(board)
    if empty_pos==False:
        return True
    for i in range(1,10):
        if validBoard(board,empty_pos,str(i)):
            board[empty_pos[0]][empty_pos[1]] = str(i)
            val = backtracksudoku(board)
            if val:
                return True
        board[empty_pos[0]][empty_pos[1]] = str(".")
    return False

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]== ".":
                return [i,j]
    return False

def validBoard(board,pos,num):
    col = pos[0]
    row = pos[1]
    for i in range(len(board)):
        if board[col][i]==num and [col,i]!=pos:
            return False
    
    for i in range(len(board[0])):
        if board[i][row]==num and [i,row]!=pos:
            return False
    
    grid_row = row//3
    grid_col = col//3
    for i in range(grid_row*3,grid_row*3+3):
        for j in range(grid_col*3,grid_col*3+3):
            if board[j][i]==num and [i,j]!=pos:
                return False
            
    return True
class Solver:
    def solveSudoku(self,board) :
        global res
        res = board
        backtracksudoku(res)
        return res
        # print_sudoku(res)

    def print_sudoku(self,board):
        for i in range(len(board)):
            flag=0
            for j in range(len(board[0])):
                if j%3==0 and j!=0:
                    print(" | ",end=board[i][j]+" ")
                elif i%3==0 and i!=0 and flag==0:
                    flag=1
                    print("------------------------")
                    print(board[i][j],end=" ")
                else:
                    print(board[i][j],end=" ")
            print()