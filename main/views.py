from django.shortcuts import render
from django.http import JsonResponse
from algorithm import sudoku_solver, sudoku_maker

def index(request):
    print(request)
    return render(request, "main/index.html")

def solve_sudoku(request):
    init_arr = sudoku_maker.run_make_arr()
    result = sudoku_solver.run_cpp_program(init_arr)
    print(request)
    return JsonResponse({'result': result})

# def make_init_arr(request):
#     arr = sudoku_maker.run_make_arr()
#     print(request)
#     return JsonResponse({'arr' : arr})