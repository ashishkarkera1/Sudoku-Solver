from django.shortcuts import render,redirect,HttpResponse

# Create your views here.
def index(request):
    return redirect("app/sudokusolver")

def SudokuSolver(request):
    return render(request,"sudoku.html")

def Algorithm(request):
    return render(request,"sudokualgorithm.html")

def About(request):
    return render(request,"about.html")

def testing(request):
    return render(request,"testing.html")

