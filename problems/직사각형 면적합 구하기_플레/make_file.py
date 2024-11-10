import make_testcase
import answer_seg
import os
import zipfile

output_dir = "직사각형 면적합 구하기 test_case"
os.makedirs(output_dir, exist_ok=True)

with zipfile.ZipFile(f"{output_dir}/test_case.zip", 'w') as zipf:
    cnt = 1
    for j in range(1, 2): # n=1~10 인 경우가 각 3번씩 만들어지게
        for i in range(9995, 10000): # n=1~10인 경우

            # .in 파일 생성
            first_file = f"{output_dir}/{cnt}.in"
            with open(first_file, 'w') as f:
                num = make_testcase.Calculate(i)
                board = num.values()
                board.insert(0, [0,0,0,0])

                # f.write(' '.join(map(str, board))) # 숫자형 리스트를 문자열 리스트로
                f.write(str(i) + '\n')
                for row in board[1:]:
                    f.write(' '.join(map(str, row)) + '\n')
                print(board)
            
            # .out 파일 생성
            second_file = f"{output_dir}/{cnt}.out"
            with open(second_file, 'w') as ff:
                ff.write(str(answer_seg.ans(i, board[1:]))) 

            zipf.write(first_file, arcname=f"{cnt}.in")
            zipf.write(second_file, arcname=f"{cnt}.out")
            cnt += 1

            os.remove(first_file)
            os.remove(second_file)

print("zip 파일 생성")
