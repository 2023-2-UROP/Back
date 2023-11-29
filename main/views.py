from django.shortcuts import render
from django.http import JsonResponse
import re
from algorithm import sudoku_solver, sudoku_maker
import subprocess

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
            # 클라이언트에서 전송한 파일은 'image' 키를 통해 얻을 수 있습니다.
            uploaded_file = request.FILES['image']

            # 서버에 저장할 파일 경로를 지정합니다.
            # 여기서는 'imgtoarr/' 디렉토리에 클라이언트에서 업로드한 파일 이름으로 저장합니다.
            file_path = 'imgtoarr/' + uploaded_file.name

            # 파일을 바이너리 쓰기 모드로 열고, 업로드된 파일의 데이터를 쓰기합니다.
            with open(file_path, 'wb') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)

            # 파일 저장이 완료되면 main.py를 실행합니다.
            # result = subprocess.run(["python", "/Users/zsu/mysite/imgtoarr/main.py"])
            # result = subprocess.run(["python", "imgtoarr/main.py"], capture_output=True, text=True)
            stdout = subprocess.PIPE, stderr = subprocess.PIPE, text = True
            result = subprocess.run(["python", "imgtoarr/main.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                    text=True)
            # numbers = re.findall(r'\b\d+\b', result.stdout)

            # 필요한 정보를 추출하여 딕셔너리로 변환
            result_dict = {
                # 'returncode': result.returncode,
                'stdout': result.stdout,
                # 'stderr': result.stderr
            }

            # 딕셔너리를 JSON으로 변환
            result_json = json.dumps(result_dict)
            # result = subprocess.run(["python", "/Users/zsu/PycharmProjects/pythonProject2/imgtoarr/main.py"])

            # 성공 응답을 반환합니다.
            return JsonResponse({'status': 'success' , 'result' : result_json})
        except Exception as e:
            # 예외가 발생한 경우 에러 응답을 반환합니다.
            return JsonResponse({'status': 'error', 'message': str(e)})

    # POST 메서드가 아닌 경우에는 잘못된 요청 메시지를 반환합니다.
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

