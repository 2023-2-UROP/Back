import subprocess
def run_make_arr():
    try:
        subprocess.run(["g++", "algorithm/make_arr.cpp", "-o", "sudoku_maker"], check=True)
        process = subprocess.Popen(
            ["./sudoku_maker"],
            # stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        stdout, stderr = process.communicate()
        return stdout
    except subprocess.CalledProcessError as e:
        return f"C++ compilation failed: {e}"
    except Exception as e:
        return f"An error occurred: {e}"

# if __name__ == "__main__":
#     result = run_make_arr()
#     lines = result.strip().split("\n")
#
#     # 각 줄을 공백으로 분리하고, 각 문자열을 int로 변환하여 2차원 리스트로 만듭니다.
#     sudoku_int = [[int(num) for num in line.split()] for line in lines]
#
#     # print(type(result))
#     print(result)
#     # print(sudoku_int)
#     output_str = ""
#
#     for row in sudoku_int:
#         row_str = " ".join(map(str, row))
#         output_str += row_str + "\n"  # 줄바꿈 문자를 추가
#
#     print(output_str)
#     print(type(output_str))
