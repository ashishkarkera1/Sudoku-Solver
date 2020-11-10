from django.shortcuts import render,HttpResponse
import json
from handler.sudoku_solver import Solver
# Create your views here.
def SolveSudoku(request):
    #get all values and arrange them in the required structure

    board = []
    pointer = 0
    for _ in range(9):
        inner = []
        for _ in range(9):
            inner.append(request.POST.get("cell-"+str(pointer)) if request.POST.get("cell-"+str(pointer))!="" else ".")
            pointer+=1
        board.append(inner)
    # board = [["9","8",".","6",".",".",".","3","1"],
    #          [".",".","7",".",".",".",".",".","."],
    #          ["6",".",".","5","4",".",".",".","."],
    #          [".",".",".",".",".","8","3","7","4"],
    #          [".",".",".",".","6",".",".",".","."],
    #          [".",".",".",".",".",".","9",".","2"],
    #          [".","3","2",".",".","7","4",".","."],
    #          [".","4",".","3",".",".",".","1","."],
    #          [".",".",".",".",".",".",".",".","."]
    #          ]
    print(board)
    #call the algorithm

    solver = Solver()
    solved_board = solver.solveSudoku(board)
    solver.print_sudoku(solved_board)
    #Convert to required response format
    
    response = {}
    pointer = 0
    for i in range(len(solved_board)):
        for j in range(len(solved_board[0])):
            response["cell"+str(pointer)] = solved_board[i][j]
            pointer+=1
    #return the ajax response

    return HttpResponse(json.dumps(response))