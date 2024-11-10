import make_testcase
import answer
import os
import zipfile

output_dir = "전력 공급 test_case"
os.makedirs(output_dir, exist_ok=True)

with zipfile.ZipFile(f"{output_dir}/test_case.zip", 'w') as zipf:
    for cnt in range(1, 10):
        # .in 파일 생성
        first_file = f"{output_dir}/{cnt}.in"
        with open(first_file, 'w') as f:
            row_values, matrix = make_testcase.Calculate(cnt).values()
            print(row_values)
            print(matrix)
            for num in row_values:
                f.write(f"{num}\n")
            
            for node_cost in matrix:
                f.write(" ".join(map(str, node_cost)) + '\n')
        
        # .out 파일 생성
        second_file = f"{output_dir}/{cnt}.out"
        with open(second_file, 'w') as ff:
            ff.write(str(answer.func(row_values, matrix)))
        
        zipf.write(first_file, arcname=f"{cnt}.in")
        zipf.write(second_file, arcname=f"{cnt}.out")
        os.remove(first_file)
        os.remove(second_file)
#----------------------------------------------------------#
    # for i in range(1, 31):
    #     # .in 파일 생성
    #     first_file = f"{output_dir}/{cnt}.in"
    #     with open(first_file, 'w') as f:
    #         num = make_SM_testcase.Calculate(i)
    #         string_res = num.values()
    #         f.write(string_res)
        
    #     # .out 파일 생성
    #     second_file = f"{output_dir}/{cnt}.out"
    #     with open(second_file, 'w') as ff:
    #         ff.write(str(answer.ans(i, string_res)))
        
    #     zipf.write(first_file, arcname=f"{cnt}.in")
    #     zipf.write(second_file, arcname=f"{cnt}.out")
    #     cnt+=1
    #     os.remove(first_file)
    #     os.remove(second_file)


print("zip 파일 생성")
