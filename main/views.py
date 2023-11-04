from django.shortcuts import render
from django.http import JsonResponse
from algorithm import sudoku_solver, sudoku_maker
import json
def index(request):
    print(request)
    return render(request, "main/index.html")

def get_sudoku_arr(request):
    arr = sudoku_maker.run_make_arr()
    print(request)
    arr = arr.strip().split("\n")
    arr = [[int(num) for num in line.split()] for line in arr]
    return JsonResponse({'arr' : arr})


def solve_sudoku(request):
    if request.method == "POST":
        body = json.loads(request.body.decode('utf-8'))
        # .decode('utf-8') -> 바이트 문자열을 'utf-8'인코딩을 사용해 xq표준 python 문자열 str로 디코딩
        # .loads -> JSON 형식의 문자열을 python 딕서너리로 변환
        arr = body.get('arr', [])
        result = sudoku_solver.run_cpp_program(arr)
        return JsonResponse({'result': result})

