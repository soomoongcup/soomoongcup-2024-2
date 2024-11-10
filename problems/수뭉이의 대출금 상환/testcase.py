import pathlib
import random

# 이 파일과 동일한 폴더에 oj.py가 있어야 합니다.
# oj.py 주소: https://gist.github.com/hepheir/c4c6326c48b1af344196c1d115d4eca1

from oj import Problem


BASE_DIR = pathlib.Path(__file__).parent.resolve()

SOLUTION_FILE = BASE_DIR/"solution.py"
TESTCASE_DIR = BASE_DIR/"testcase"
TESTCASE_ZIP_FILE = BASE_DIR/"loan.zip"


###############################################################
# 테스트케이스 생성
###############################################################

problem = Problem(answer_file=SOLUTION_FILE)


# 예제 테스트케이스 생성

random.seed(0)
T = random.randint(1, 1000)

with problem.testcase("1") as sys:
    lines = [
        "5",
        "2.00 1000.00 100.00",
        "5.00 2000.00 500.00",
        "1.00 5000.00 50.00",
        "10.00 1000.00 50.00",
        "1.00 100.00 102.00",
    ]
    sys.stdin.write("\n".join(lines))


# 랜덤 테스트케이스 생성

MIN_R = 0
MAX_R = 50

MIN_B = 0.00
MAX_B = 50000.00


def random_float(min_val: int, max_val: int) -> float:
    return random.randint(min_val*100, max_val*100)/100


with problem.testcase("2") as sys:
    sys.stdin.write(f'{T}\n')
    for i in range(T):
        R = random_float(int(MIN_R), int(MAX_R)) # 0.00~50.00
        B = random_float(int(MIN_B), int(MAX_B))
        M = random_float(int(MIN_B), int(MAX_B))
        sys.stdin.write(f"{R} {B} {M}\n")


# 생성한 테스트케이스 저장

problem.save(zipname=TESTCASE_ZIP_FILE, dirname=TESTCASE_DIR)
