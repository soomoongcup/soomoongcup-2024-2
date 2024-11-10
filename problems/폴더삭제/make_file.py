import make_testcase
import answer
import os
import zipfile

output_dir = "파일삭제 test_case"
os.makedirs(output_dir, exist_ok=True)

with zipfile.ZipFile(f"{output_dir}/test_case.zip", 'w') as zipf:
    cnt = 1
    for i in range(1, 31): # 30개 생성
        wallpaper = []
        # .in 파일 생성
        first_file = f"{output_dir}/{cnt}.in"
        with open(first_file, 'w') as f:
            res_list = make_testcase.Calculate(i)
            res = res_list.values()
            for row in res:
                if isinstance(row, list):
                    f.write(' '.join(map(str, row)) + '\n')
                else:
                    f.write(row + '\n')
            wallpaper = res[1:]


        # .out 파일 생성
        second_file = f"{output_dir}/{cnt}.out"
        with open(second_file, 'w') as ff:
            ff.write(str(answer.func(wallpaper)))
        
        zipf.write(first_file, arcname=f"{cnt}.in")
        zipf.write(second_file, arcname=f"{cnt}.out")
        cnt+=1
        os.remove(first_file)
        os.remove(second_file)

print("zip 파일 생성")