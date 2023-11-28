from django.shortcuts import render
from django.http import JsonResponse
from algorithm import sudoku_solver, sudoku_maker
from django.views.decorators.csrf import csrf_exempt
import base64
from PIL import Image
from io import BytesIO
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

# def img_to_arr(request):
#     if request.method == "POST":
#         try:
#             image_data = request.body
#             # with open(image_data, 'rb') as f:
#             #     image_data = f.read()
#             image_data_decoded = base64.b64decode(image_data)
#
#             # image_data_decoded = base64.b64decode(image_data)
#
#             # 파일로 저장하여 확인
#             with open('received_image.png', 'wb') as f:
#                 f.write(image_data_decoded)
#             return JsonResponse({'status': 'success'})
#         except Exception as e:
#             return JsonResponse({'status': 'error', 'message': str(e)})
#
#     return JsonResponse({'status': 'error', 'message': 'Invalid request method'})


def img_to_arr(request):
    if request.method == "POST":
        try:
            uploaded_file = request.FILES['image']
            with open('ar/' + uploaded_file.name, 'wb') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)

            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})